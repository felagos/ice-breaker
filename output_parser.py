from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class PersonIntel(BaseModel):
    summary: str = Field(description="Summary of person")
    facts: List[str] = Field(description="Interesting facts about person")
    topics_of_interest: List[str] = Field(
        description="Topics of interest of person")
    ice_breaker:  List[str] = Field(description="Ice breaker for person")

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breaker": self.ice_breaker,
        }


person_intel_parser: PydanticOutputParser = PydanticOutputParser(pydantic_object=PersonIntel)
