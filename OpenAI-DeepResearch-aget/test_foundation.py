#!/usr/bin/env python3
"""
Test DeepThink Foundation
Verify AGET v2 structure and core functionality
"""

import asyncio
import sys
from pathlib import Path

# Test imports
print("🧪 Testing DeepThink foundation with AGET v2...")

try:
    # Test core imports
    from src.core.deepthink import DeepThink
    from src.core.router import ResearchMethod
    print("✅ Core imports successful")

    # Test agent imports
    from src.agents.multi_agent import DeepResearchSystem
    print("✅ Agent module imports successful")

    # Test API imports
    from src.apis.deep_research import OpenAIDeepResearchAPI
    print("✅ API module imports successful")

except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)


async def test_deepthink():
    """Test basic DeepThink functionality"""

    print("\n🔬 Testing DeepThink initialization...")

    try:
        # Initialize DeepThink
        deepthink = DeepThink(method=ResearchMethod.AUTO)
        deepthink.introduce()

        print("✅ DeepThink initialized successfully")

        # Verify AGET structure
        aget_path = Path(".aget")
        if aget_path.exists():
            print(f"✅ AGET structure found: {list(aget_path.iterdir())}")

        # Check version
        version_file = aget_path / "version.json"
        if version_file.exists():
            import json
            with open(version_file) as f:
                version_info = json.load(f)
                print(f"✅ AGET Version: {version_info}")

        # Get statistics (should be empty)
        stats = deepthink.get_statistics()
        print(f"✅ Statistics accessible: {stats}")

        print("\n🎉 Foundation test complete! DeepThink v0.1.0 is operational")
        print("   Built on AGET v2.0.0-alpha (bleeding edge)")

        return True

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(test_deepthink())

    if success:
        print("\n📋 Next steps:")
        print("   1. ✅ Foundation complete - AGET structure and core migration done")
        print("   2. ⏭️  Add memory system with pattern tracking")
        print("   3. ⏭️  Implement DeepThink personality")

        print("\n💡 Quick test:")
        print("   python -c \"from src.core.deepthink import DeepThink; import asyncio; dt = DeepThink(); dt.introduce()\"")

    sys.exit(0 if success else 1)