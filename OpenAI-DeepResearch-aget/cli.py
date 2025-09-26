#!/usr/bin/env python3
"""
CLI for OpenAI-DeepResearch-aget
Command-line interface with personality
"""

import sys
import asyncio
import json
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.personality.wake_up import DeepResearchAgent


async def main():
    """Main CLI entry point"""

    agent = DeepResearchAgent()

    # Parse command
    if len(sys.argv) < 2:
        # No arguments - show wake-up
        await agent.wake_up()
        return

    command = sys.argv[1].lower()

    if command == "wake" or command == "wake-up":
        await agent.wake_up()

    elif command == "intro":
        agent.quick_intro()

    elif command == "stats":
        show_stats()

    elif command == "insights":
        show_insights()

    elif command == "wind-down":
        await agent.wind_down()

    elif command == "help":
        show_help()

    else:
        # Assume it's a research query
        query = " ".join(sys.argv[1:])
        await research_query(query, agent)


def show_stats():
    """Show statistics from memory"""
    print("\n📊 OpenAI-DeepResearch-aget Statistics")
    print("="*40)

    stats_file = Path(".aget/memory/stats.json")
    patterns_file = Path(".aget/memory/patterns.json")

    if stats_file.exists():
        with open(stats_file) as f:
            stats = json.load(f)

        print(f"Total queries: {stats.get('total_queries', 0)}")
        print(f"Average response time: {stats.get('avg_response_time', 0):.1f}s")
        print(f"Cache hits: {stats.get('cache_hits', 0)}")
        print(f"Patterns learned: {stats.get('patterns_learned', 0)}")

        if patterns_file.exists():
            with open(patterns_file) as f:
                patterns = json.load(f)

            # Analyze patterns
            methods = {}
            for p in patterns:
                method = p.get('method', 'unknown')
                methods[method] = methods.get(method, 0) + 1

            print(f"\nMethod distribution:")
            for method, count in methods.items():
                print(f"  • {method}: {count} uses")
    else:
        print("No statistics available yet. Start making queries!")


def show_insights():
    """Show insights from patterns"""
    print("\n🧠 OpenAI-DeepResearch-aget Insights")
    print("="*40)

    patterns_file = Path(".aget/memory/patterns.json")

    if patterns_file.exists():
        with open(patterns_file) as f:
            patterns = json.load(f)

        if patterns:
            # Query type analysis
            query_types = {}
            for p in patterns:
                qt = p.get('query_type', 'unknown')
                query_types[qt] = query_types.get(qt, 0) + 1

            print("Query types processed:")
            for qt, count in sorted(query_types.items(), key=lambda x: x[1], reverse=True):
                print(f"  • {qt}: {count}")

            # Best performing patterns
            print("\nSuccessful patterns learned:")
            success_patterns = {}
            for p in patterns:
                if p.get('success'):
                    pattern = f"{p.get('query_type')} → {p.get('method')}"
                    success_patterns[pattern] = success_patterns.get(pattern, 0) + 1

            for pattern, count in sorted(success_patterns.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"  • {pattern}: {count} successes")

            # Performance insights
            total_time = sum(p.get('response_time', 0) for p in patterns)
            avg_time = total_time / len(patterns) if patterns else 0
            print(f"\nPerformance:")
            print(f"  • Average response: {avg_time:.1f}s")
            print(f"  • Total patterns: {len(patterns)}")
        else:
            print("No patterns learned yet.")
    else:
        print("No insights available yet. Start making queries!")


async def research_query(query, agent):
    """Simulate a research query"""
    print(f"\n🔍 Research Query: {query}")
    print("-"*40)

    # Quick intro
    agent.quick_intro()

    print(f"\nProcessing query...")
    print("(In production, this would call the actual research system)")

    # For now, just show what would happen
    # Direct import to avoid router import issues
    import sys
    sys.path.insert(0, str(Path(__file__).parent / 'src' / 'core'))
    import memory
    mem = memory.ResearchMemory()

    # Get suggestion from memory
    suggestion = mem.suggest_method(query)
    if suggestion:
        print(f"📚 Memory suggests: {suggestion}")
    else:
        print(f"🤔 No pattern match - will use auto-routing")

    # Check cache
    cached = mem.get_cached_result(query)
    if cached:
        print(f"⚡ Found in cache! Returning cached result...")
    else:
        print(f"🔬 Would execute research using appropriate method...")

    print(f"\n[Research would happen here in production]")
    print(f"For now, use the original OpenAI_DeepResearch scripts")


def show_help():
    """Show help message"""
    print("\n📚 OpenAI-DeepResearch-aget Help")
    print("="*40)
    print("\nCommands:")
    print("  wake, wake-up     - Show full wake-up sequence")
    print("  intro            - Quick introduction")
    print("  stats            - Show performance statistics")
    print("  insights         - Show learned patterns and insights")
    print("  wind-down        - Wind down the agent")
    print("  help             - Show this help message")
    print("  [query]          - Research a topic (simulation)")
    print("\nExamples:")
    print("  python cli.py wake")
    print("  python cli.py stats")
    print("  python cli.py \"What is a transformer?\"")
    print()


if __name__ == "__main__":
    asyncio.run(main())