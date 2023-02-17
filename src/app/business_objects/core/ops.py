from abc import ABCMeta, abstractmethod


# =========================================================
# CLASS BUSINESS OPERATION
# =========================================================
class BusinessOperation:
    """
    Top level class that represents an operation
    (transaction)
    """

    __metaclass__ = ABCMeta

    # -----------------------------------------------------
    # PROPERTY OPERATION RESULT
    # -----------------------------------------------------
    @property
    @abstractmethod
    def operation_result(self) -> any:
        pass

    # -----------------------------------------------------
    # METHOD PERFORM TRANSACTION
    # -----------------------------------------------------
    @abstractmethod
    def perform_transaction(self):
        pass
