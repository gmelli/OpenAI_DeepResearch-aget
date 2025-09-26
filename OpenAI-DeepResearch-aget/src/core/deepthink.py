#!/usr/bin/env python3
"""
DeepThink Core - Enhanced Research Router with AGET v2 patterns
"""

import asyncio
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

from .router import ResearchInterface, ResearchMethod, UnifiedResearchResult


class DeepThink(ResearchInterface):
    """DeepThink cognitive research agent"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "DeepThink"
        self.version = "0.1.0"
        self.aget_version = "2.0.0-alpha"
        self.route_history = []
        self.evolution_dir = Path(".aget/evolution")
        self.evolution_dir.mkdir(parents=True, exist_ok=True)

        print(f"🧠 {self.name} v{self.version} initializing...")
        print(f"   Built with AGET v{self.aget_version} (bleeding edge)")

    async def research(self, query: str, method: Optional[ResearchMethod] = None, verbose: bool = True, **kwargs) -> UnifiedResearchResult:
        """Enhanced research with decision tracking"""

        start_time = time.time()

        # Track decision
        decision_context = {
            "query": query,
            "timestamp": datetime.now().isoformat(),
            "method_override": method is not None
        }

        # Perform research using parent class
        result = await super().research(query, method, verbose, **kwargs)

        # Record routing decision
        elapsed = time.time() - start_time
        self._record_routing_decision(decision_context, result, elapsed)

        # Add DeepThink metadata
        result.metadata["agent"] = self.name
        result.metadata["version"] = self.version
        result.metadata["elapsed_time"] = elapsed

        return result

    def _record_routing_decision(self, context: Dict, result: UnifiedResearchResult, elapsed: float):
        """Record routing decision for evolution tracking"""

        decision = {
            "timestamp": context["timestamp"],
            "query": context["query"],
            "method_selected": result.method_used,
            "was_override": context["method_override"],
            "success": True,  # TODO: Implement success detection
            "elapsed_seconds": elapsed,
            "citations_count": result.metadata.get("citations_count", 0)
        }

        self.route_history.append(decision)

        # Save to evolution if significant
        if len(self.route_history) % 5 == 0:  # Every 5 decisions
            self._save_evolution_entry(decision)

    def _save_evolution_entry(self, decision: Dict):
        """Save decision to evolution tracking"""

        entry = {
            "type": "ROUTING_DECISION",
            "timestamp": decision["timestamp"],
            "agent": f"{self.name} v{self.version}",
            "decision": decision,
            "pattern_detected": self._detect_pattern(decision)
        }

        # Save to daily evolution file
        today = datetime.now().strftime("%Y-%m-%d")
        evolution_file = self.evolution_dir / f"{today}-routing.json"

        entries = []
        if evolution_file.exists():
            with open(evolution_file) as f:
                entries = json.load(f)

        entries.append(entry)

        with open(evolution_file, "w") as f:
            json.dump(entries, f, indent=2)

    def _detect_pattern(self, decision: Dict) -> Optional[Dict]:
        """Detect patterns in routing decisions"""

        # Simple pattern detection for now
        query = decision["query"].lower()

        if any(word in query for word in ["landscape", "comprehensive", "analyze"]):
            return {
                "type": "comprehensive_analysis",
                "confidence": 0.8,
                "suggested_method": "deep_research_api"
            }
        elif any(word in query for word in ["how to", "implement", "code"]):
            return {
                "type": "technical_question",
                "confidence": 0.75,
                "suggested_method": "openai_agents"
            }

        return None

    def get_statistics(self) -> Dict[str, Any]:
        """Get DeepThink statistics"""

        if not self.route_history:
            return {"message": "No research performed yet"}

        total = len(self.route_history)
        methods_used = {}
        total_time = 0
        total_citations = 0

        for decision in self.route_history:
            method = decision["method_selected"]
            methods_used[method] = methods_used.get(method, 0) + 1
            total_time += decision["elapsed_seconds"]
            total_citations += decision["citations_count"]

        return {
            "total_queries": total,
            "avg_response_time": total_time / total,
            "total_citations": total_citations,
            "methods_distribution": methods_used,
            "preferred_method": max(methods_used, key=methods_used.get),
            "agent": self.name,
            "version": self.version
        }

    def introduce(self):
        """DeepThink introduces itself"""
        print(f"\n🧠 Hello! I'm {self.name}, your cognitive research companion.")
        print(f"   I combine OpenAI's Agents orchestration with Deep Research API")
        print(f"   to provide comprehensive, intelligent research assistance.")
        print(f"   I learn from every interaction to serve you better!\n")

        stats = self.get_statistics()
        if stats.get("total_queries"):
            print(f"📊 So far, I've handled {stats['total_queries']} queries")
            print(f"   with an average response time of {stats['avg_response_time']:.1f}s\n")


async def main():
    """Test DeepThink foundation"""

    deepthink = DeepThink()
    deepthink.introduce()

    # Test basic research
    print("🔍 Testing basic research capability...")
    result = await deepthink.research(
        "What is a transformer architecture?",
        method=ResearchMethod.OPENAI_AGENTS
    )

    print(f"✅ Research complete!")
    print(f"   Method: {result.method_used}")
    print(f"   Time: {result.metadata['elapsed_time']:.2f}s")
    print(f"   Preview: {result.result[:200]}...")

    # Show statistics
    stats = deepthink.get_statistics()
    print(f"\n📊 Statistics: {json.dumps(stats, indent=2)}")


if __name__ == "__main__":
    asyncio.run(main())