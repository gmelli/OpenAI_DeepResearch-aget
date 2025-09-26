#!/usr/bin/env python3
"""
DeepThink with Memory - Cognitive Research Agent that Learns
"""

import asyncio
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

from .router import ResearchInterface, ResearchMethod, UnifiedResearchResult
from .memory import ResearchMemory


class DeepThinkWithMemory(ResearchInterface):
    """DeepThink enhanced with memory and learning capabilities"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "DeepThink"
        self.version = "0.2.0"  # Upgraded with memory
        self.aget_version = "2.0.0-alpha"

        # Initialize memory system
        self.memory = ResearchMemory()

        # Evolution tracking
        self.evolution_dir = Path(".aget/evolution")
        self.evolution_dir.mkdir(parents=True, exist_ok=True)

        print(f"🧠 {self.name} v{self.version} initializing with memory...")
        print(f"   {len(self.memory.patterns)} patterns remembered from previous sessions")

    async def research(self, query: str, method: Optional[ResearchMethod] = None, verbose: bool = True, **kwargs) -> UnifiedResearchResult:
        """Research with memory-enhanced routing"""

        start_time = time.time()

        # Check cache first
        cached_result = self.memory.get_cached_result(query)
        if cached_result:
            return cached_result

        # Get memory suggestion if no method specified
        if not method:
            suggested_method = self.memory.suggest_method(query)
            if suggested_method:
                # Convert string to ResearchMethod enum
                if suggested_method == "openai_agents":
                    method = ResearchMethod.OPENAI_AGENTS
                elif suggested_method == "deep_research_api":
                    method = ResearchMethod.DEEP_RESEARCH_API

        # Track decision context
        decision_context = {
            "query": query,
            "timestamp": datetime.now().isoformat(),
            "method_override": method is not None,
            "memory_suggestion": self.memory.suggest_method(query)
        }

        if verbose and decision_context["memory_suggestion"]:
            print(f"🧠 Memory suggests: {decision_context['memory_suggestion']}")

        # Perform research
        try:
            result = await super().research(query, method, verbose, **kwargs)
            success = True
        except Exception as e:
            print(f"❌ Research failed: {e}")
            success = False
            # Create error result
            result = UnifiedResearchResult(
                query=query,
                method_used="failed",
                result=f"Research failed: {str(e)}",
                metadata={"error": str(e)}
            )

        elapsed = time.time() - start_time

        # Remember this query
        self.memory.remember_query(
            query=query,
            method=result.method_used,
            success=success,
            response_time=elapsed,
            citations_count=result.metadata.get("citations_count", 0)
        )

        # Cache successful results
        if success:
            self.memory.cache_result(query, result)

        # Add DeepThink metadata
        result.metadata["agent"] = self.name
        result.metadata["version"] = self.version
        result.metadata["elapsed_time"] = elapsed
        result.metadata["memory_active"] = True

        # Record significant decisions
        if len(self.memory.patterns) % 10 == 0:
            self._record_learning_milestone()

        return result

    def _record_learning_milestone(self):
        """Record learning milestones in evolution"""
        insights = self.memory.get_insights()

        milestone = {
            "type": "LEARNING_MILESTONE",
            "timestamp": datetime.now().isoformat(),
            "agent": f"{self.name} v{self.version}",
            "patterns_learned": insights["patterns_learned"],
            "total_patterns": insights["total_patterns"],
            "cache_hit_rate": insights["cache_hit_rate"],
            "insights": insights
        }

        # Save to evolution
        today = datetime.now().strftime("%Y-%m-%d")
        evolution_file = self.evolution_dir / f"{today}-learning.json"

        entries = []
        if evolution_file.exists():
            with open(evolution_file) as f:
                entries = json.load(f)

        entries.append(milestone)

        with open(evolution_file, 'w') as f:
            json.dump(entries, f, indent=2)

        print(f"📈 Learning milestone recorded: {insights['patterns_learned']} patterns learned")

    def get_memory_insights(self) -> Dict[str, Any]:
        """Get insights from memory"""
        return self.memory.get_insights()

    def introduce_with_memory(self):
        """Introduce DeepThink with memory context"""
        print(f"\n🧠 Hello! I'm {self.name} v{self.version}, your cognitive research companion.")
        print(f"   I combine OpenAI's Agents orchestration with Deep Research API")
        print(f"   and I learn from every interaction to serve you better!\n")

        insights = self.get_memory_insights()

        if insights.get("total_patterns", 0) > 0:
            print(f"📚 Memory Status:")
            print(f"   • {insights['total_patterns']} patterns remembered")
            print(f"   • {insights['patterns_learned']} patterns learned")
            print(f"   • {insights['cache_hit_rate']} cache hit rate")
            print(f"   • {insights['avg_response_time']} average response time")

            if insights.get("method_preferences"):
                preferred = max(insights["method_preferences"], key=insights["method_preferences"].get)
                print(f"   • Preferred method: {preferred}")

            if insights.get("best_combinations"):
                print(f"\n🎯 Best learned combinations:")
                for combo, stats in list(insights["best_combinations"].items())[:3]:
                    print(f"   • {combo}: {stats['count']} successes, {stats['avg_time']:.1f}s avg")
        else:
            print(f"📚 Ready to learn from our interactions!")

        print()

    def cleanup_memory(self, max_age_hours: int = 24):
        """Clean old volatile memory"""
        return self.memory.cleanup_volatile(max_age_hours)


async def test_memory_system():
    """Test the memory-enhanced DeepThink"""

    print("🧪 Testing DeepThink with Memory System...\n")

    # Initialize DeepThink with memory
    deepthink = DeepThinkWithMemory(method=ResearchMethod.AUTO)
    deepthink.introduce_with_memory()

    # Simulate some queries to build memory
    test_queries = [
        ("What is a transformer architecture?", ResearchMethod.OPENAI_AGENTS),
        ("How to implement error handling in Python?", ResearchMethod.OPENAI_AGENTS),
        ("Comprehensive analysis of LLM frameworks", ResearchMethod.DEEP_RESEARCH_API),
    ]

    print("📝 Simulating queries to build memory...\n")

    for query, expected_method in test_queries:
        print(f"Query: {query[:50]}...")

        # Simulate research (without actual API calls for testing)
        result = UnifiedResearchResult(
            query=query,
            method_used=expected_method.value,
            result=f"Simulated result for: {query}",
            metadata={"citations_count": 10, "simulated": True}
        )

        # Remember the pattern
        deepthink.memory.remember_query(
            query=query,
            method=expected_method.value,
            success=True,
            response_time=2.5,
            citations_count=10
        )

        # Cache the result
        deepthink.memory.cache_result(query, result)

        print(f"✅ Learned: {deepthink.memory._classify_query(query)} → {expected_method.value}\n")

    # Test memory suggestions
    print("🎯 Testing memory suggestions:\n")

    test_suggestion_queries = [
        "How to handle exceptions in JavaScript?",  # Should suggest OPENAI_AGENTS
        "Analyze the competitive landscape of AI tools",  # Should suggest DEEP_RESEARCH_API
    ]

    for query in test_suggestion_queries:
        suggestion = deepthink.memory.suggest_method(query)
        print(f"Query: {query}")
        print(f"Memory suggests: {suggestion or 'No suggestion yet'}\n")

    # Show insights
    print("📊 Memory Insights:")
    insights = deepthink.get_memory_insights()
    print(json.dumps(insights, indent=2))

    # Test cache
    print("\n⚡ Testing cache:")
    cached = deepthink.memory.get_cached_result(test_queries[0][0])
    if cached:
        print(f"Successfully retrieved cached result!")

    print("\n✅ Memory system test complete!")
    print(f"   • {len(deepthink.memory.patterns)} patterns in memory")
    print(f"   • {insights.get('patterns_learned', 0)} patterns learned")
    print(f"   • Cache working: {cached is not None}")

    return True


if __name__ == "__main__":
    asyncio.run(test_memory_system())