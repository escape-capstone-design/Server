from pydantic import BaseModel, field_validator


class GetFeedbackRequest(BaseModel):
    question: str
    answer: str
    student_answer: str

    @field_validator('question', 'answer','student_answer')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v