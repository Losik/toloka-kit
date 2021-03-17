from enum import Enum
from typing import Any, Dict, Optional

from .primitives.base import BaseTolokaObject
from .primitives.operators import (
    ComparableConditionMixin,
    CompareOperator,
    IdentityConditionMixin,
    IdentityOperator
)


class RuleConditionKey(Enum):
    ...

class RuleCondition(BaseTolokaObject):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,*,
        operator: Optional[Any] = ...,
        value: Optional[Any] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: Optional[Any]
    value: Optional[Any]

class ComparableRuleCondition(RuleCondition, ComparableConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,*,
        value: Optional[Any] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    value: Optional[Any]
    operator: CompareOperator

class IdentityRuleCondition(RuleCondition, IdentityConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: IdentityOperator,*,
        value: Optional[Any] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    value: Optional[Any]
    operator: IdentityOperator

class AcceptedAssignmentsCount(ComparableRuleCondition):
    """How many times this assignment was accepted

    Don't be confused!!!
    This condition used only with 'AssignmentsAssessment' controller.
    And exist very similar condition 'AssignmentsAcceptedCount', that used only with 'AnswerCount' controller.
    Sorry about that.
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class AcceptedAssignmentsRate(ComparableRuleCondition):
    """Percentage of how many assignments were accepted from this performer out of all checked assignment
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[float]

class AssessmentEvent(IdentityRuleCondition):
    """Assessment of the assignment changes its status to the specified one

    This condition can work only with compare operator '=='.

    Attributes:
        value: Possible values:
            * conditions.AssessmentEvent.ACCEPT
            * conditions.AssessmentEvent.REJECT
    
    Example:
        How to increase task overlap when you reject assignment in delayed mode.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AssignmentsAssessment(),
        >>>     conditions=[toloka.conditions.AssessmentEvent == toloka.conditions.AssessmentEvent.REJECT],
        >>>     action=toloka.actions.ChangeOverlap(delta=1, open_pool=True),
        >>> )
        ...
    """

    class Type(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: IdentityOperator,
        value: Optional[Type] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: Optional[Type]

class AssignmentsAcceptedCount(ComparableRuleCondition):
    """How many assignment was accepted from performer

    Don't be confused!!!
    This condition used only with 'AnswerCount' controller.
    And exist very similar condition 'AcceptedAssignmentsCount', that used only with 'AssignmentsAssessment' controller.
    Sorry about that.
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class CorrectAnswersRate(ComparableRuleCondition):
    """The percentage of correct responses

    Be careful, it may have different meanings in different collectors.
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[float]

class FailRate(ComparableRuleCondition):
    """Percentage of wrong answers of the performer to the captcha
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[float]

class FastSubmittedCount(ComparableRuleCondition):
    """The number of assignments a specific performer completed too fast
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class GoldenSetAnswersCount(ComparableRuleCondition):
    """The number of completed control tasks
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class GoldenSetCorrectAnswersRate(ComparableRuleCondition):
    """The percentage of correct responses in control tasks
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[float]

class GoldenSetIncorrectAnswersRate(ComparableRuleCondition):
    """The percentage of incorrect responses in control tasks
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[float]

class IncomeSumForLast24Hours(ComparableRuleCondition):
    """The performer earnings for completed tasks in the pool over the last 24 hours
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[float]

class IncorrectAnswersRate(ComparableRuleCondition):
    """The percentage of incorrect responses

    Be careful, it may have different meanings in different collectors.
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[float]

class NextAssignmentAvailable(ComparableRuleCondition):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[bool] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[bool]

class PendingAssignmentsCount(ComparableRuleCondition):
    """Number of Assignments pending checking 
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class PoolAccessRevokedReason(IdentityRuleCondition):
    """Reason for loss of access of the performer to the current pool

    Attributes:
        value: exact reason
            * SKILL_CHANGE - The performer no longer meets one or more filters.
            * RESTRICTION - The performer's access to tasks is blocked by a quality control rule (such as control tasks,
                majority vote, fast answers, skipped assignments, or captcha).
    """

    class Type(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: IdentityOperator,
        value: Optional[Type] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: Optional[Type]

class RejectedAssignmentsCount(ComparableRuleCondition):
    """How many times this assignment was rejected
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class RejectedAssignmentsRate(ComparableRuleCondition):
    """Percentage of how many assignments were rejected from this performer out of all checked assignment
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[float]

class SkillId(IdentityRuleCondition):
    """The performer no longer meets the specific skill filter
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: IdentityOperator,
        value: Optional[str] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: Optional[str]

class SkippedInRowCount(ComparableRuleCondition):
    """How many tasks in a row the performer skipped
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class StoredResultsCount(ComparableRuleCondition):
    """How many times the performer entered captcha
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class SubmittedAssignmentsCount(ComparableRuleCondition):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class SuccessRate(ComparableRuleCondition):
    """Percentage of correct answers of the performer to the captcha
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[float]

class TotalAnswersCount(ComparableRuleCondition):
    """The number of completed tasks by the performer

    Be careful, it may have different meanings in different collectors.
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class TotalAssignmentsCount(ComparableRuleCondition):
    """How many assignments from this performer were checked
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class TotalSubmittedCount(ComparableRuleCondition):
    """The number of assignments a specific performer completed
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]
