from enum import Enum

class EventStatus(str, Enum):
    DRAFT = "draft"
    OPEN_FOR_PROPOSAL = "open_for_proposal"
    SCHEDULED = "scheduled"
    COMPLETED = "completed"