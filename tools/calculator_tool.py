"""
Calculator tool for the AI Customer Support Agent.

This module provides safe arithmetic evaluation.
The LLM should never perform mathematical calculations directly.
"""

from __future__ import annotations

import ast
import operator

from utils.exceptions import CalculatorError
from utils.logger import get_logger

logger = get_logger(__name__)


_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def _evaluate(expression: str) -> float:
    """
    Safely evaluate a mathematical expression.

    Parameters
    ----------
    expression:
        Arithmetic expression.

    Returns
    -------
    float
        Calculation result.
    """

    tree = ast.parse(
        expression,
        mode="eval",
    )

    def evaluate_node(node: ast.AST) -> float:
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return float(node.value)

            raise ValueError("Invalid number.")

        if isinstance(node, ast.BinOp):
            operation = _ALLOWED_OPERATORS.get(
                type(node.op)
            )

            if operation is None:
                raise ValueError("Unsupported operator.")

            return operation(
                evaluate_node(node.left),
                evaluate_node(node.right),
            )

        if isinstance(node, ast.UnaryOp):
            operation = _ALLOWED_OPERATORS.get(
                type(node.op)
            )

            if operation is None:
                raise ValueError("Unsupported operator.")

            return operation(
                evaluate_node(node.operand)
            )

        raise ValueError("Invalid expression.")

    return evaluate_node(tree.body)


def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.

    Parameters
    ----------
    expression:
        User calculation request.

    Returns
    -------
    str
        Formatted result.
    """

    try:
        logger.info(
            "Calculating expression: %s",
            expression,
        )

        result = _evaluate(expression)

        return str(result)

    except Exception as exc:
        logger.exception(
            "Calculator failed."
        )

        raise CalculatorError(
            f"Unable to calculate expression: {exc}"
        ) from exc