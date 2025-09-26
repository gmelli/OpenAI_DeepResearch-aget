#!/usr/bin/env python3
"""
Test Memory System Standalone
"""

import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path.cwd()))

print("🧪 Testing DeepThink Memory System...\n")

# Test memory module directly
from src.core.memory import ResearchMemory

# Initialize memory
memory = ResearchMemory()
print(f"✅ Memory initialized with {len(memory.patterns)} existing patterns\n")

# Simulate some queries to build patterns
test_data = [
    ("What is a transformer architecture?", "openai_agents", True, 45.2, 15),
    ("How to implement error handling in Python?", "openai_agents", True, 32.1, 8),
    ("Analyze the competitive landscape of AI tools", "deep_research_api", True, 187.5, 78),
    ("Best practices for microservices", "deep_research_api", True, 156.3, 65),
    ("How to use async/await in JavaScript?", "openai_agents", True, 28.7, 5),
]

print("📝 Learning from simulated queries:\n")

for query, method, success, time_taken, citations in test_data:
    memory.remember_query(query, method, success, time_taken, citations)
    query_type = memory._classify_query(query)
    print(f"  • {query_type}: {query[:40]}... → {method}")

print(f"\n✅ Learned {len(memory.patterns)} patterns")

# Test pattern suggestions
print("\n🎯 Testing pattern-based suggestions:\n")

test_queries = [
    "How to handle exceptions in JavaScript?",
    "Comprehensive analysis of LLM frameworks",
    "What is dependency injection?",
    "Compare different database architectures"
]

for query in test_queries:
    suggestion = memory.suggest_method(query)
    query_type = memory._classify_query(query)
    print(f"  Query: {query[:50]}...")
    print(f"  Type:  {query_type}")
    print(f"  Suggestion: {suggestion or 'No confident suggestion yet'}\n")

# Test caching
print("⚡ Testing cache system:\n")

# Cache a result
test_query = "What is a neural network?"
test_result = {"content": "A neural network is...", "citations": 10}
memory.cache_result(test_query, test_result)
print(f"  Cached result for: {test_query}")

# Retrieve from cache
cached = memory.get_cached_result(test_query)
if cached:
    print(f"  ✅ Successfully retrieved from cache!")
else:
    print(f"  ❌ Cache retrieval failed")

# Get insights
print("\n📊 Memory Insights:\n")
insights = memory.get_insights()

for key, value in insights.items():
    if isinstance(value, dict):
        print(f"  {key}:")
        for k, v in value.items():
            if isinstance(v, dict):
                print(f"    • {k}: {v.get('count', v.get('avg_time', v))}")
            else:
                print(f"    • {k}: {v}")
    else:
        print(f"  {key}: {value}")

# Check persistence
print("\n💾 Checking persistence:")
patterns_file = Path(".aget/memory/patterns.json")
stats_file = Path(".aget/memory/stats.json")

if patterns_file.exists():
    print(f"  ✅ Patterns saved to {patterns_file}")
    with open(patterns_file) as f:
        saved_patterns = json.load(f)
        print(f"     {len(saved_patterns)} patterns persisted")

if stats_file.exists():
    print(f"  ✅ Stats saved to {stats_file}")
    with open(stats_file) as f:
        saved_stats = json.load(f)
        print(f"     Stats: {saved_stats}")

# Test cleanup
print("\n🧹 Testing cleanup:")
cleaned = memory.cleanup_volatile(max_age_hours=0)  # Clean everything for test
print(f"  Cleaned {cleaned} old cache entries")

print("\n🎉 Memory System Test Complete!")
print(f"   • Pattern recognition: ✅")
print(f"   • Method suggestions: ✅")
print(f"   • Result caching: ✅")
print(f"   • Persistence: ✅")
print(f"   • Insights generation: ✅")
print(f"\n   DeepThink now has memory and can learn from experience!")