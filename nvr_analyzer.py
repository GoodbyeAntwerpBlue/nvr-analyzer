#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NVR 消费决策分析工具
Need-Value-Return Analysis Tool

一个帮助你做出理性消费决策的命令行工具
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Tuple


class NVRAnalyzer:
    """NVR模型分析器"""
    
    # 七个维度的定义
    DIMENSIONS = {
        '安全': {'icon': '🛡️', 'weight_base': 1.5, 'desc': '降低风险与焦虑'},
        '健康': {'icon': '💪', 'weight_base': 1.5, 'desc': '维持身体能量'},
        '时间': {'icon': '⏰', 'weight_base': 1.5, 'desc': '节约或创造时间'},
        '自由': {'icon': '🗝️', 'weight_base': 1.2, 'desc': '扩展选择与自主权'},
        '连接': {'icon': '🤝', 'weight_base': 1.0, 'desc': '建立情感联结'},
        '成长': {'icon': '🌱', 'weight_base': 1.2, 'desc': '提升能力与认知'},
        '意义': {'icon': '✨', 'weight_base': 1.0, 'desc': '精神满足感'}
    }
    
    def __init__(self, data_file='nvr_records.json'):
        """初始化"""
        self.data_file = data_file
        self.records = self.load_records()
    
    def load_records(self) -> List[Dict]:
        """加载历史记录"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_records(self):
        """保存记录"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.records, f, ensure_ascii=False, indent=2)
    
    def get_number_input(self, prompt: str, min_val: float = 0, max_val: float = 10) -> float:
        """获取数字输入（带验证）"""
        while True:
            try:
                value = input(prompt).strip()
                if value == '':
                    return 0
                value = float(value)
                if min_val <= value <= max_val:
                    return value
                print(f"⚠️  请输入 {min_val}-{max_val} 之间的数字")
            except ValueError:
                print("⚠️  请输入有效的数字")
    
    def print_header(self, text: str):
        """打印标题"""
        print("\n" + "="*60)
        print(f"  {text}")
        print("="*60)
    
    def print_section(self, text: str):
        """打印章节"""
        print(f"\n{'─'*60}")
        print(f"  {text}")
        print(f"{'─'*60}")
    
    def assess_need(self) -> Tuple[Dict[str, float], float]:
        """评估需求矩阵"""
        self.print_section("第一步：评估你的需求 (Need Matrix)")
        print("\n请为每个维度打分 (0-10分，0=不需要，10=极度需要)")
        print("提示：可以直接回车跳过（默认为0）\n")
        
        needs = {}
        weighted_needs = {}
        
        for dim, info in self.DIMENSIONS.items():
            print(f"\n{info['icon']} {dim}：{info['desc']}")
            score = self.get_number_input(f"   你的需求强度 (0-10): ")
            needs[dim] = score
            weighted_needs[dim] = score * info['weight_base']
        
        total_need = sum(weighted_needs.values())
        
        # 显示汇总
        self.print_section("你的需求汇总")
        print(f"\n{'维度':<8} {'需求分':<8} {'权重':<8} {'加权需求':<10}")
        print("─"*50)
        for dim, score in needs.items():
            weight = self.DIMENSIONS[dim]['weight_base']
            weighted = weighted_needs[dim]
            print(f"{dim:<6} {score:>6.1f}   {weight:>6.1f}   {weighted:>8.1f}")
        print("─"*50)
        print(f"{'总需求分':<6} {' ':>6}   {' ':>6}   {total_need:>8.1f}")
        
        return weighted_needs, total_need
    
    def assess_value(self, product_name: str, price: float) -> Tuple[Dict[str, float], float, float]:
        """评估价值矩阵"""
        self.print_section("第二步：评估产品价值 (Value Matrix)")
        print(f"\n产品：{product_name}")
        print(f"价格：¥{price:,.2f}")
        print("\n请评估这个产品在每个维度能提供的价值 (0-10分)")
        print("提示：0=无价值，5=一般，10=卓越\n")
        
        values = {}
        
        for dim, info in self.DIMENSIONS.items():
            print(f"\n{info['icon']} {dim}：{info['desc']}")
            score = self.get_number_input(f"   产品价值 (0-10): ")
            values[dim] = score
        
        total_value = sum(values.values())
        value_density = total_value / (price / 10000) if price > 0 else 0
        
        # 显示汇总
        self.print_section("产品价值汇总")
        print(f"\n{'维度':<8} {'价值分':<10}")
        print("─"*30)
        for dim, score in values.items():
            print(f"{dim:<6} {score:>8.1f}")
        print("─"*30)
        print(f"{'总价值分':<6} {total_value:>8.1f}")
        print(f"\n价值密度 = {total_value:.1f} / {price/10000:.1f}万 = {value_density:.2f}")
        
        return values, total_value, value_density
    
    def calculate_match(self, weighted_needs: Dict[str, float], values: Dict[str, float]) -> Tuple[float, Dict[str, float]]:
        """计算匹配度"""
        matches = {}
        total_match = 0
        
        for dim in self.DIMENSIONS.keys():
            match = weighted_needs[dim] * values[dim]
            matches[dim] = match
            total_match += match
        
        # 理论最大值：所有维度都是10×权重×10
        max_possible = sum(10 * info['weight_base'] * 10 for info in self.DIMENSIONS.values())
        match_percentage = (total_match / max_possible) * 100
        
        return match_percentage, matches
    
    def calculate_roi(self, match_percentage: float, value_density: float) -> float:
        """计算性价比指数"""
        return (match_percentage / 100) * value_density
    
    def get_recommendation(self, roi: float) -> Tuple[str, str, str]:
        """获取推荐建议"""
        if roi >= 1.5:
            return "🟢 强烈推荐", "buy", "这个产品非常适合你的需求，性价比极高！"
        elif roi >= 1.0:
            return "🟡 可以考虑", "consider", "这个产品基本符合需求，建议对比其他方案后再决定。"
        else:
            return "🔴 不推荐", "reject", "这个产品与你的需求匹配度较低，建议重新考虑。"
    
    def check_impulse_buying(self) -> bool:
        """冲动消费检测"""
        self.print_section("冲动消费检测")
        print("\n请诚实回答以下问题（y/n）：\n")
        
        questions = [
            "1. 这是你当天突然想买的吗？",
            "2. 是因为打折/限量/网红推荐才心动的吗？",
            "3. 购买前有情绪波动（生气/焦虑/孤独）吗？",
            "4. 你家里有类似的东西正在闲置吗？"
        ]
        
        red_flags = 0
        for q in questions:
            answer = input(f"{q} (y/n): ").strip().lower()
            if answer == 'y':
                red_flags += 1
        
        if red_flags >= 2:
            print("\n⚠️  警告：检测到冲动消费风险！建议延迟48小时后再决定。")
            return True
        else:
            print("\n✅ 通过冲动检测")
            return False
    
    def time_decay_test(self) -> str:
        """时间衰减测试"""
        self.print_section("时间衰减测试")
        print("\n请预测这个产品的价值会如何随时间变化：\n")
        print("1. 🔺 增值型 - 使用越久价值越高（如技能培训、工具）")
        print("2. ➡️ 稳定型 - 长期提供稳定价值（如家具、基础设施）")
        print("3. 🔻 衰减型 - 短暂兴奋后迅速贬值（如潮流单品）")
        print("4. ⚡ 即时型 - 当下体验，无残留价值（如娱乐消费）")
        
        choice = input("\n请选择 (1-4): ").strip()
        
        types = {
            '1': ('🔺 增值型', 1.5),
            '2': ('➡️ 稳定型', 1.0),
            '3': ('🔻 衰减型', 0.5),
            '4': ('⚡ 即时型', 0.3)
        }
        
        return types.get(choice, types['2'])
    
    def show_detailed_analysis(self, weighted_needs: Dict, values: Dict, matches: Dict):
        """显示详细分析"""
        self.print_section("详细匹配度分析")
        
        print(f"\n{'维度':<8} {'你的需求':<10} {'产品价值':<10} {'匹配分':<10} {'匹配度'}")
        print("─"*60)
        
        sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)
        
        for dim, match_score in sorted_matches:
            need = weighted_needs[dim]
            value = values[dim]
            # 匹配度百分比（相对于该维度的最大值）
            max_dim = 10 * self.DIMENSIONS[dim]['weight_base'] * 10
            match_pct = (match_score / max_dim) * 100 if max_dim > 0 else 0
            
            bar = '█' * int(match_pct / 10)
            print(f"{dim:<6} {need:>8.1f}   {value:>8.1f}   {match_score:>8.1f}   {bar} {match_pct:.0f}%")
        
        print("─"*60)
        
        # 分析高匹配和低匹配维度
        high_match = [dim for dim, score in sorted_matches[:3]]
        low_match = [dim for dim, score in sorted_matches[-3:] if score < 20]
        
        print(f"\n✅ 高匹配维度：{', '.join(high_match)}")
        if low_match:
            print(f"⚠️  低匹配维度：{', '.join(low_match)}")
    
    def run_analysis(self):
        """运行完整分析"""
        self.print_header("💰 NVR 消费决策分析工具")
        print("\n欢迎使用！让我们一起做出理性的消费决策。\n")
        
        # 基本信息
        product_name = input("📦 产品/服务名称: ").strip()
        if not product_name:
            print("❌ 产品名称不能为空")
            return
        
        price = self.get_number_input("💵 价格 (元): ", min_val=0, max_val=10000000)
        if price <= 0:
            print("❌ 价格必须大于0")
            return
        
        # 第一步：需求评估
        weighted_needs, total_need = self.assess_need()
        
        # 第二步：价值评估
        values, total_value, value_density = self.assess_value(product_name, price)
        
        # 第三步：匹配度计算
        self.print_section("第三步：匹配度计算 (Fit Analysis)")
        match_percentage, matches = self.calculate_match(weighted_needs, values)
        
        # 详细分析
        self.show_detailed_analysis(weighted_needs, values, matches)
        
        print(f"\n总匹配度 = {match_percentage:.1f}%")
        
        # 计算ROI
        roi = self.calculate_roi(match_percentage, value_density)
        print(f"性价比指数 = {match_percentage:.1f}% × {value_density:.2f} = {roi:.2f}")
        
        # 时间衰减测试
        time_type, time_coefficient = self.time_decay_test()
        adjusted_roi = roi * time_coefficient
        
        print(f"\n时间类型：{time_type}")
        print(f"调整后性价比指数 = {roi:.2f} × {time_coefficient} = {adjusted_roi:.2f}")
        
        # 冲动消费检测
        is_impulse = self.check_impulse_buying()
        
        # 最终决策
        self.print_header("✨ 决策建议")
        recommendation, decision, reason = self.get_recommendation(adjusted_roi)
        
        print(f"\n{recommendation}")
        print(f"\n性价比指数：{adjusted_roi:.2f}")
        print(f"决策建议：{reason}")
        
        if is_impulse:
            print("\n⚠️  强烈建议：延迟48小时后重新评估此决策！")
        
        # 保存记录
        record = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'product': product_name,
            'price': price,
            'needs': dict(weighted_needs),
            'values': values,
            'match_percentage': match_percentage,
            'value_density': value_density,
            'roi': adjusted_roi,
            'time_type': time_type,
            'decision': decision,
            'is_impulse': is_impulse
        }
        
        self.records.append(record)
        self.save_records()
        
        print(f"\n✅ 决策记录已保存到 {self.data_file}")
    
    def view_history(self):
        """查看历史记录"""
        if not self.records:
            print("\n暂无历史记录")
            return
        
        self.print_header("📊 历史决策记录")
        
        print(f"\n{'序号':<6} {'日期':<20} {'产品':<20} {'价格':<12} {'ROI':<8} {'决策'}")
        print("─"*90)
        
        for i, record in enumerate(self.records[-20:], 1):  # 显示最近20条
            decision_icon = {
                'buy': '🟢',
                'consider': '🟡',
                'reject': '🔴'
            }.get(record.get('decision', 'consider'), '🟡')
            
            print(f"{i:<6} {record['date']:<20} {record['product'][:18]:<20} "
                  f"¥{record['price']:>10,.2f} {record['roi']:>6.2f}   {decision_icon}")
        
        print("\n💡 提示：输入序号查看详情，输入 0 返回主菜单")
        
        choice = input("\n请选择: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(self.records[-20:]):
            self.show_record_detail(self.records[-(21-int(choice))])
    
    def show_record_detail(self, record: Dict):
        """显示记录详情"""
        self.print_header(f"📄 {record['product']} - 详细信息")
        
        print(f"\n日期：{record['date']}")
        print(f"价格：¥{record['price']:,.2f}")
        print(f"匹配度：{record['match_percentage']:.1f}%")
        print(f"价值密度：{record['value_density']:.2f}")
        print(f"性价比指数：{record['roi']:.2f}")
        print(f"时间类型：{record.get('time_type', '未知')}")
        
        print("\n需求分布：")
        for dim, score in record['needs'].items():
            bar = '█' * int(score / 2)
            print(f"  {dim}: {bar} {score:.1f}")
        
        print("\n价值分布：")
        for dim, score in record['values'].items():
            bar = '█' * int(score)
            print(f"  {dim}: {bar} {score:.1f}")
        
        input("\n按回车返回...")
    
    def show_statistics(self):
        """显示统计信息"""
        if not self.records:
            print("\n暂无数据")
            return
        
        self.print_header("📈 消费决策统计")
        
        total = len(self.records)
        buy_count = sum(1 for r in self.records if r.get('decision') == 'buy')
        consider_count = sum(1 for r in self.records if r.get('decision') == 'consider')
        reject_count = sum(1 for r in self.records if r.get('decision') == 'reject')
        
        total_spent = sum(r['price'] for r in self.records if r.get('decision') == 'buy')
        total_saved = sum(r['price'] for r in self.records if r.get('decision') == 'reject')
        
        avg_roi = sum(r['roi'] for r in self.records) / total if total > 0 else 0
        
        print(f"\n总决策次数：{total}")
        print(f"  🟢 推荐购买：{buy_count} ({buy_count/total*100:.1f}%)")
        print(f"  🟡 可以考虑：{consider_count} ({consider_count/total*100:.1f}%)")
        print(f"  🔴 不推荐：{reject_count} ({reject_count/total*100:.1f}%)")
        
        print(f"\n预计支出：¥{total_spent:,.2f}")
        print(f"避免支出：¥{total_saved:,.2f}")
        print(f"平均ROI：{avg_roi:.2f}")
        
        # 需求分析
        print("\n你最关注的维度 TOP 3：")
        dim_needs = {dim: [] for dim in self.DIMENSIONS.keys()}
        for record in self.records:
            for dim, score in record['needs'].items():
                dim_needs[dim].append(score)
        
        avg_needs = {dim: sum(scores)/len(scores) for dim, scores in dim_needs.items() if scores}
        top_dims = sorted(avg_needs.items(), key=lambda x: x[1], reverse=True)[:3]
        
        for dim, avg in top_dims:
            print(f"  {self.DIMENSIONS[dim]['icon']} {dim}: {avg:.1f}")
        
        input("\n按回车返回...")


def main():
    """主菜单"""
    analyzer = NVRAnalyzer()
    
    while True:
        print("\n" + "="*60)
        print("  💰 NVR 消费决策分析工具")
        print("="*60)
        print("\n请选择功能：")
        print("  1. 🆕 开始新的消费决策分析")
        print("  2. 📊 查看历史记录")
        print("  3. 📈 查看统计信息")
        print("  4. ❌ 退出")
        
        choice = input("\n请输入选项 (1-4): ").strip()
        
        if choice == '1':
            analyzer.run_analysis()
        elif choice == '2':
            analyzer.view_history()
        elif choice == '3':
            analyzer.show_statistics()
        elif choice == '4':
            print("\n👋 感谢使用！理性消费，智慧生活！")
            break
        else:
            print("\n⚠️  无效选项，请重新选择")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 已退出程序")
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
