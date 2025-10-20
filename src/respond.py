from typing import Any
from dataclasses import dataclass
import json

@dataclass
class TaskMeta:
    task_id: str
    agent_git_url: str
    dataset_name: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "agent_git_url": self.agent_git_url,
            "dataset_name": self.dataset_name
        }

@dataclass
class Respond:
    task_meta: TaskMeta = None
    dataset_size: int = None
    error: str = None
    messages: dict = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_meta": self.task_meta.to_dict() if self.task_meta else None,
            "dataset_size": self.dataset_size,
            "error": self.error,
            "messages": self.messages
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


# mock evaluation results

mock_evaluation_results = {
  "total_score": 0.2546074092904365,
  "total_tasks": 3,
  "successful_tasks": 3,
  "failed_tasks": 0,
  "results": [
    {
      "task_id": "task_1_1760932220",
      "question": "What is the date when the US SEC approved Bitcoin spot ETF?",
      "category": "web_retrieval",
      "evaluation_method": "rule_based",
      "agent_response": "The US SEC approved Bitcoin spot ETF on January 10, 2024 (UTC).",
      "evaluation_score": 0.25354478434681893,
      "evaluation_reasoning": "Multi-dimensional evaluation: factual_accuracy=0.00, completeness=1.00, precision=0.15, relevance=0.24, conciseness=1.00; Base score: 0.21, Confidence factor: 1.18; ",
      "confidence": 0.95,
      "processing_time": 0.5013635158538818,
      "tools_used": [
        "web_search",
        "blockchain_query",
        "data_analysis"
      ],
      "status": "completed"
    },
    {
      "task_id": "task_2_1760932223",
      "question": "What is the date of Ethereum Shapella mainnet upgrade?",
      "category": "web_retrieval",
      "evaluation_method": "llm_based",
      "agent_response": "Ethereum Shapella mainnet upgrade occurred on April 12, 2023 (UTC).",
      "evaluation_score": 0.173,
      "evaluation_reasoning": "LLM evaluation failed: Error code: 401 - {'error': {'message': 'Incorrect API key provided: your-api*****here. You can find your API key at https://platform.openai.com/account/api-keys.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_api_key'}}\nExpected answer analysis: 0.29 (exact_match: False, key_info: 0.58, factual: 0.57, completeness: 0.00)",
      "confidence": 0.92,
      "processing_time": 0.5017118453979492,
      "tools_used": [
        "web_search",
        "blockchain_query",
        "data_analysis"
      ],
      "status": "completed"
    },
    {
      "task_id": "task_3_1760932226",
      "question": "When did PayPal release PYUSD stablecoin?",
      "category": "web_onchain_retrieval",
      "evaluation_method": "hybrid",
      "agent_response": "PayPal released PYUSD stablecoin on August 7, 2023 (UTC).",
      "evaluation_score": 0.185,
      "evaluation_reasoning": "Rule-based evaluation: 0.10 (weight: 0.3); LLM evaluation: 0.00 (weight: 0.7); Comprehensive score: 0.03\nExpected answer analysis: 0.29 (exact_match: False, key_info: 0.58, factual: 0.57, completeness: 0.00)",
      "confidence": 0.88,
      "processing_time": 0.5040991306304932,
      "tools_used": [
        "web_search",
        "blockchain_query",
        "data_analysis"
      ],
      "status": "completed"
    }
  ]
}