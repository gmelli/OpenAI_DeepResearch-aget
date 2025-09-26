#!/usr/bin/env python3
"""
Wake-Up Protocol for OpenAI-DeepResearch-aget
Agent personality for managing the OpenAI_DeepResearch system
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# Add parent to path for imports
sys.path.append(str(Path(__file__).parent.parent))


class DeepResearchAgent:
    """Personality for the OpenAI-DeepResearch-aget cognitive agent"""

    def __init__(self):
        self.agent_name = "OpenAI-DeepResearch-aget"
        self.nickname = "DeepThink"  # Personality name
        self.version = "0.3.0"  # With personality
        self.purpose = "Managing and enhancing the OpenAI_DeepResearch dual-implementation system"

        # Load state
        self.load_agent_state()

    def load_agent_state(self):
        """Load agent state and context"""
        # Version info
        version_file = Path(".aget/version.json")
        if version_file.exists():
            with open(version_file) as f:
                self.version_info = json.load(f)
        else:
            self.version_info = {"version": self.version, "aget_version": "2.0.0-alpha"}

        # Memory stats
        self.memory_stats = self.load_memory_stats()

        # Evolution tracking
        self.evolution_entries = self.count_evolution_entries()

    def load_memory_stats(self) -> Dict[str, Any]:
        """Load memory statistics"""
        stats_file = Path(".aget/memory/stats.json")
        patterns_file = Path(".aget/memory/patterns.json")

        stats = {
            "patterns": 0,
            "total_queries": 0,
            "avg_response_time": 0,
            "cache_hits": 0
        }

        if patterns_file.exists():
            with open(patterns_file) as f:
                patterns = json.load(f)
                stats["patterns"] = len(patterns)

        if stats_file.exists():
            with open(stats_file) as f:
                saved_stats = json.load(f)
                stats.update(saved_stats)

        return stats

    def count_evolution_entries(self) -> int:
        """Count evolution entries"""
        evolution_dir = Path(".aget/evolution")
        if evolution_dir.exists():
            return len(list(evolution_dir.glob("*.json")) + list(evolution_dir.glob("*.md")))
        return 0

    async def wake_up(self):
        """Wake-up sequence for OpenAI-DeepResearch-aget"""

        print("\n" + "="*60)
        print("🧠 OpenAI-DeepResearch-aget Awakening...")
        print("="*60 + "\n")

        # Introduction
        print(f"Hello! I'm {self.nickname}, the cognitive agent managing your")
        print("OpenAI_DeepResearch dual-implementation research system.\n")

        print(f"📚 Purpose: {self.purpose}")
        print(f"🔧 Version: {self.version} | AGET {self.version_info.get('aget_version', 'unknown')}")

        # System Status
        print("\n" + "-"*40)
        print("📊 System Status")
        print("-"*40)

        # Check components
        print("\n✅ Core Components:")
        components = [
            ("OpenAI Agents System", Path("src/agents/multi_agent.py").exists()),
            ("Deep Research API", Path("src/apis/deep_research.py").exists()),
            ("Intelligent Router", Path("src/core/router.py").exists()),
            ("Memory System", Path("src/core/memory.py").exists()),
            ("Personality Module", True)  # We're running!
        ]

        for component, status in components:
            status_icon = "✓" if status else "✗"
            print(f"  [{status_icon}] {component}")

        # Memory Status
        print(f"\n📚 Memory Status:")
        print(f"  • Patterns learned: {self.memory_stats['patterns']}")
        print(f"  • Total queries processed: {self.memory_stats['total_queries']}")

        if self.memory_stats['avg_response_time'] > 0:
            print(f"  • Average response time: {self.memory_stats['avg_response_time']:.1f}s")

        if self.memory_stats['total_queries'] > 0:
            cache_rate = (self.memory_stats['cache_hits'] / self.memory_stats['total_queries']) * 100
            print(f"  • Cache hit rate: {cache_rate:.1f}%")

        # Evolution Status
        print(f"\n🔬 Evolution Tracking:")
        print(f"  • Decisions recorded: {self.evolution_entries}")

        # Personality traits
        print("\n" + "-"*40)
        print("🎭 Agent Personality")
        print("-"*40)
        print("\nI approach research with these traits:")
        print("  • Meticulous - Every detail matters in research")
        print("  • Learning-oriented - I improve with each query")
        print("  • Efficient - I cache and reuse knowledge")
        print("  • Adaptive - I choose the best method for each query")

        # Capabilities
        print("\n" + "-"*40)
        print("💡 Capabilities")
        print("-"*40)
        print("\n  🔍 Research Methods:")
        print("     • OpenAI Agents - Fast technical queries (30-60s)")
        print("     • Deep Research API - Comprehensive analysis (2-5min)")
        print("     • Auto-routing based on learned patterns")

        print("\n  🧠 Cognitive Features:")
        print("     • Pattern recognition from past queries")
        print("     • Result caching for instant responses")
        print("     • Evolution tracking for continuous improvement")
        print("     • Performance insights and statistics")

        # Ready message
        print("\n" + "="*60)
        print("✨ OpenAI-DeepResearch-aget is ready!")
        print("="*60)
        print("\nTry: python cli.py \"Your research question here\"")
        print("     python cli.py stats  # View performance statistics")
        print("     python cli.py insights  # See learned patterns\n")

    async def wind_down(self):
        """Wind-down sequence"""
        print("\n" + "-"*40)
        print("🌙 Winding Down OpenAI-DeepResearch-aget")
        print("-"*40)

        # Save any pending memory
        print("💾 Saving memory patterns...")

        # Report session stats
        print(f"📊 Session complete:")
        print(f"   • Patterns in memory: {self.memory_stats['patterns']}")
        print(f"   • Evolution entries: {self.evolution_entries}")

        print("\n\"Every research query makes me smarter. See you next session!\"")
        print("   - DeepThink, your OpenAI_DeepResearch agent\n")

    def quick_intro(self):
        """Quick introduction for CLI"""
        print(f"🧠 {self.nickname} v{self.version} - OpenAI_DeepResearch Cognitive Agent")
        if self.memory_stats['patterns'] > 0:
            print(f"   {self.memory_stats['patterns']} patterns learned | Ready to research!")
        else:
            print(f"   Ready to learn from your research queries!")


# Test the personality
if __name__ == "__main__":
    import asyncio

    agent = DeepResearchAgent()

    # Run wake-up sequence
    asyncio.run(agent.wake_up())

    # Show quick intro
    print("\n" + "="*60)
    print("Quick intro mode:")
    print("-"*40)
    agent.quick_intro()

    # Wind down
    asyncio.run(agent.wind_down())