import ast
import asyncio
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).parent / "custom_components" / "priceanalyzer"


def test_setup_does_not_wait_for_price_downloads():
    sensor_source = (ROOT / "sensor.py").read_text()
    integration_source = (ROOT / "__init__.py").read_text()

    assert "await self._data.check_stuff()" not in sensor_source
    assert "entry.async_create_background_task(" in integration_source


def test_legacy_string_version_migrates_to_int():
    flow_tree = ast.parse((ROOT / "config_flow.py").read_text())
    version_class = next(
        node
        for node in flow_tree.body
        if isinstance(node, ast.ClassDef) and node.name == "_ConfigFlowVersion"
    )
    namespace = {}
    exec(compile(ast.Module([version_class], []), "config_flow.py", "exec"), namespace)
    current_version = namespace["_ConfigFlowVersion"](1)

    assert isinstance(current_version, int)
    assert "1.0" != current_version
    assert not "1.0" > current_version

    integration_tree = ast.parse((ROOT / "__init__.py").read_text())
    migrate_function = next(
        node
        for node in integration_tree.body
        if isinstance(node, ast.AsyncFunctionDef) and node.name == "async_migrate_entry"
    )
    namespace = {"HomeAssistant": object, "ConfigEntry": object}
    exec(
        compile(ast.Module([migrate_function], []), "__init__.py", "exec"),
        namespace,
    )

    entry = SimpleNamespace(version="1.0")
    config_entries = SimpleNamespace(
        async_update_entry=lambda entry, *, version: setattr(entry, "version", version)
    )
    assert asyncio.run(
        namespace["async_migrate_entry"](SimpleNamespace(config_entries=config_entries), entry)
    )
    assert entry.version == 1


if __name__ == "__main__":
    test_setup_does_not_wait_for_price_downloads()
    test_legacy_string_version_migrates_to_int()
