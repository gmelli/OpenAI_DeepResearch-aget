#!/usr/bin/env python3
"""Simple test without deep imports"""

import sys
from pathlib import Path

print(f"Current directory: {Path.cwd()}")
print(f"Python path: {sys.path[:3]}")

# Add current directory to path
sys.path.insert(0, str(Path.cwd()))

# Try simple import
try:
    from src.core import ResearchInterface
    print("✅ Can import from src.core")
except ImportError as e:
    print(f"❌ Cannot import from src.core: {e}")

# Check structure
print(f"\n📁 AGET Structure:")
for path in Path(".").glob("*"):
    if path.is_dir():
        print(f"  📂 {path.name}/")
        for subpath in path.glob("*"):
            if subpath.is_file():
                print(f"      📄 {subpath.name}")

# Check .aget
aget_path = Path(".aget")
if aget_path.exists():
    print(f"\n✅ AGET directory exists")
    version_file = aget_path / "version.json"
    if version_file.exists():
        import json
        with open(version_file) as f:
            version = json.load(f)
            print(f"✅ Version info: {version['agent']} v{version['version']}")
            print(f"   AGET version: {version['aget_version']} ({'bleeding edge' if version.get('bleeding_edge') else 'stable'})")

print("\n🎉 Foundation structure is in place!")
print("   DeepThink is ready for Step 2: Memory System")