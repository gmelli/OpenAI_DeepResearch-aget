#!/usr/bin/env python3
"""
Memory System for DeepThink
Persistent patterns and volatile cache with learning capabilities
"""

import json
import hashlib
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any


class ResearchMemory:
    """Hybrid memory system for DeepThink - persistent patterns and volatile cache"""

    def __init__(self, aget_dir: str = ".aget", workspace_dir: str = "workspace"):
        # Persistent memory (backed up, git-tracked)
        self.persistent_dir = Path(aget_dir) / "memory"
        self.persistent_dir.mkdir(parents=True, exist_ok=True)

        # Volatile memory (can be cleared)
        self.volatile_dir = Path(workspace_dir) / "memory"
        self.cache_dir = self.volatile_dir / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Load existing memories
        self.patterns = self._load_patterns()
        self.cache = {}  # In-memory cache for speed
        self.stats = self._load_stats()

        print(f"📚 Memory initialized: {len(self.patterns)} patterns loaded")

    def _load_patterns(self) -> List[Dict]:
        """Load learned patterns from persistent memory"""
        patterns_file = self.persistent_dir / "patterns.json"
        if patterns_file.exists():
            with open(patterns_file) as f:
                return json.load(f)
        return []

    def _save_patterns(self):
        """Save patterns to persistent memory"""
        patterns_file = self.persistent_dir / "patterns.json"
        with open(patterns_file, 'w') as f:
            json.dump(self.patterns, f, indent=2)

    def _load_stats(self) -> Dict:
        """Load statistics from memory"""
        stats_file = self.persistent_dir / "stats.json"
        if stats_file.exists():
            with open(stats_file) as f:
                return json.load(f)
        return {
            "total_queries": 0,
            "cache_hits": 0,
            "patterns_learned": 0,
            "avg_response_time": 0
        }

    def _save_stats(self):
        """Save statistics to persistent memory"""
        stats_file = self.persistent_dir / "stats.json"
        with open(stats_file, 'w') as f:
            json.dump(self.stats, f, indent=2)

    def remember_query(self, query: str, method: str, success: bool, response_time: float, citations_count: int = 0):
        """Remember a query and its outcome to learn patterns"""

        # Create pattern entry
        pattern = {
            "query": query,
            "query_type": self._classify_query(query),
            "method": method,
            "success": success,
            "response_time": response_time,
            "citations_count": citations_count,
            "timestamp": datetime.now().isoformat()
        }

        # Add to patterns
        self.patterns.append(pattern)

        # Update stats
        self.stats["total_queries"] += 1
        if self.stats["avg_response_time"] == 0:
            self.stats["avg_response_time"] = response_time
        else:
            # Running average
            self.stats["avg_response_time"] = (
                (self.stats["avg_response_time"] * (self.stats["total_queries"] - 1) + response_time)
                / self.stats["total_queries"]
            )

        # Learn from pattern if successful
        if success:
            self._learn_from_pattern(pattern)

        # Save periodically (every 5 queries)
        if len(self.patterns) % 5 == 0:
            self._save_patterns()
            self._save_stats()
            print(f"💾 Memory checkpoint: {len(self.patterns)} patterns saved")

    def _classify_query(self, query: str) -> str:
        """Classify query type based on keywords"""
        query_lower = query.lower()

        if any(word in query_lower for word in ["landscape", "comprehensive", "analyze", "comparison"]):
            return "comprehensive_analysis"
        elif any(word in query_lower for word in ["how to", "implement", "code", "example"]):
            return "technical_implementation"
        elif any(word in query_lower for word in ["what is", "define", "explain"]):
            return "conceptual_explanation"
        elif any(word in query_lower for word in ["best", "recommend", "should"]):
            return "recommendation"
        else:
            return "general_research"

    def _learn_from_pattern(self, pattern: Dict):
        """Learn from successful patterns"""
        query_type = pattern["query_type"]
        method = pattern["method"]

        # Count successes for this query type and method
        similar_patterns = [
            p for p in self.patterns
            if p["query_type"] == query_type and p["method"] == method and p["success"]
        ]

        if len(similar_patterns) >= 3:  # Need at least 3 successes to learn
            self.stats["patterns_learned"] += 1
            print(f"🧠 Pattern learned: {query_type} → {method} (confidence: {len(similar_patterns)/len(self.patterns):.2%})")

    def suggest_method(self, query: str) -> Optional[str]:
        """Suggest best method based on learned patterns"""
        if not self.patterns:
            return None

        query_type = self._classify_query(query)

        # Find similar successful patterns
        similar_patterns = [
            p for p in self.patterns
            if p["query_type"] == query_type and p["success"]
        ]

        if not similar_patterns:
            return None

        # Count methods
        method_scores = {}
        for pattern in similar_patterns:
            method = pattern["method"]
            if method not in method_scores:
                method_scores[method] = {"count": 0, "avg_time": 0}

            method_scores[method]["count"] += 1
            method_scores[method]["avg_time"] += pattern["response_time"]

        # Calculate average times
        for method in method_scores:
            method_scores[method]["avg_time"] /= method_scores[method]["count"]

        # Choose method with best success rate
        best_method = max(method_scores, key=lambda m: method_scores[m]["count"])
        confidence = method_scores[best_method]["count"] / len(similar_patterns)

        if confidence > 0.6:  # Only suggest if confident
            print(f"🎯 Memory suggests: {best_method} for {query_type} (confidence: {confidence:.0%})")
            return best_method

        return None

    def get_cached_result(self, query: str) -> Optional[Dict]:
        """Retrieve cached result if available and fresh"""
        query_hash = hashlib.md5(query.encode()).hexdigest()

        # Check in-memory cache first
        if query_hash in self.cache:
            cached = self.cache[query_hash]
            age = time.time() - cached["timestamp"]
            if age < 3600:  # 1 hour TTL
                self.stats["cache_hits"] += 1
                cached["hits"] += 1
                print(f"⚡ Cache hit! (used {cached['hits']} times)")
                return cached["result"]

        # Check file cache
        cache_file = self.cache_dir / f"{query_hash}.json"
        if cache_file.exists():
            with open(cache_file) as f:
                cached = json.load(f)
                age = time.time() - cached["timestamp"]
                if age < 3600:  # 1 hour TTL
                    self.stats["cache_hits"] += 1
                    self.cache[query_hash] = cached  # Load to memory
                    print(f"⚡ Cache hit from disk!")
                    return cached["result"]

        return None

    def cache_result(self, query: str, result: Any):
        """Cache research result"""
        query_hash = hashlib.md5(query.encode()).hexdigest()

        cached_data = {
            "query": query,
            "result": result,
            "timestamp": time.time(),
            "hits": 0
        }

        # Save to memory cache
        self.cache[query_hash] = cached_data

        # Save to file cache
        cache_file = self.cache_dir / f"{query_hash}.json"
        with open(cache_file, 'w') as f:
            json.dump(cached_data, f, indent=2)

    def get_insights(self) -> Dict[str, Any]:
        """Generate insights from memory"""
        if not self.patterns:
            return {"message": "No patterns learned yet"}

        # Analyze patterns
        query_types = {}
        method_preferences = {}

        for pattern in self.patterns:
            qt = pattern["query_type"]
            query_types[qt] = query_types.get(qt, 0) + 1

            if pattern["success"]:
                method = pattern["method"]
                method_preferences[method] = method_preferences.get(method, 0) + 1

        # Find best performing combinations
        best_combos = {}
        for pattern in self.patterns:
            if pattern["success"]:
                combo = f"{pattern['query_type']} → {pattern['method']}"
                if combo not in best_combos:
                    best_combos[combo] = {"count": 0, "avg_time": 0}
                best_combos[combo]["count"] += 1
                best_combos[combo]["avg_time"] += pattern["response_time"]

        for combo in best_combos:
            best_combos[combo]["avg_time"] /= best_combos[combo]["count"]

        return {
            "total_patterns": len(self.patterns),
            "patterns_learned": self.stats["patterns_learned"],
            "cache_hit_rate": f"{(self.stats['cache_hits'] / max(1, self.stats['total_queries'])) * 100:.1f}%",
            "query_types": query_types,
            "method_preferences": method_preferences,
            "best_combinations": dict(sorted(best_combos.items(), key=lambda x: x[1]["count"], reverse=True)[:3]),
            "avg_response_time": f"{self.stats['avg_response_time']:.1f}s"
        }

    def cleanup_volatile(self, max_age_hours: int = 24):
        """Clean old volatile memory"""
        cleaned = 0
        for cache_file in self.cache_dir.glob("*.json"):
            with open(cache_file) as f:
                data = json.load(f)

            age = (time.time() - data["timestamp"]) / 3600
            if age > max_age_hours:
                cache_file.unlink()
                cleaned += 1

        if cleaned > 0:
            print(f"🧹 Cleaned {cleaned} old cache entries")

        return cleaned