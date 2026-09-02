from test_suites.shared import pytest
from test_suites import (
    BaseFlow,
    AuthRegistrationTests,
    TopicTests,
    CampTests,
    StatementTests,
    ForumNewsTests,
    BrowseSearchTests,
    ProfileUploadAccessTests,
    BacklogTests,
    MiscTests,
)

class TestPages(
    BaseFlow,
    AuthRegistrationTests,
    TopicTests,
    CampTests,
    StatementTests,
    ForumNewsTests,
    BrowseSearchTests,
    ProfileUploadAccessTests,
    BacklogTests,
    MiscTests,
):
    """Composed Canonizer UI suite split by feature modules."""
    pass

def _apply_test_markers():
    """Apply consistent markers to tests so suites can be sliced by risk and speed."""
    smoke_tests = {
        "test_click_on_join_now",
        "test_click_on_login_button",
        "test_login_with_registered_credentials",
        "test_create_topic_name_with_valid_data",
        "test_create_camp_with_valid_data",
        "test_add_camp_statement_with_valid_data",
        "test_create_thread_with_valid_data",
    }
    destructive_keywords = (
        "delete",
        "remove",
        "update",
        "edit",
        "create_",
        "upload",
    )
    slow_keywords = (
        "upload",
        "search",
        "history",
        "notification",
    )

    for attr_name in dir(TestPages):
        if not attr_name.startswith("test_"):
            continue

        test_func = getattr(TestPages, attr_name)
        if not callable(test_func):
            continue

        marks = list(getattr(test_func, "pytestmark", []))

        # Every automated case belongs to baseline regression coverage.
        marks.append(pytest.mark.regression)

        if attr_name in smoke_tests:
            marks.append(pytest.mark.smoke)

        lowered = attr_name.lower()
        if any(keyword in lowered for keyword in destructive_keywords):
            marks.append(pytest.mark.destructive)

        if any(keyword in lowered for keyword in slow_keywords):
            marks.append(pytest.mark.slow)

        test_func.pytestmark = marks


_apply_test_markers()

if __name__ == "__main__":
    import sys

    raise SystemExit(pytest.main([__file__, *sys.argv[1:]]))
