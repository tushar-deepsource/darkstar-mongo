from abc import ABCMeta, abstractmethod, abstractproperty


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
    @abstractmethod
    @property
    def operation_result(self) -> any:
        pass

    # -----------------------------------------------------
    # METHOD PERFORM TRANSACTION
    # -----------------------------------------------------
    @abstractmethod
    def perform_transaction(self):
        pass
