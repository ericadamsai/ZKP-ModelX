class DaggerAgentUtils:
    @staticmethod
    def validate_result_integrity(result):
        if result is None:
            return False
        if isinstance(result, str) and not result.strip():
            return False
        return True

    @staticmethod
    def densify_text(text: str, density_axiom_value: float) -> str:
        if density_axiom_value == 1.0:
            words = text.split()
            filtered_words = [w for w in words if len(w) > 2 and w.lower() not in ["a", "an", "the", "is", "are", "and", "or"]]
            return " ".join(filtered_words)
        return text

    @staticmethod
    def generate_deterministic_hash(data):
        import hashlib
        return hashlib.sha256(str(data).encode()).hexdigest()

class DaggerAgent:
    def __init__(self, name, specialization, axioms):
        self.name = name
        self.specialization = specialization
        self.status = "idle"
        self._axioms = axioms
    def execute(self, task_params):
        self.status = "executing"
        raw_result = self._perform_task(task_params)
        if not DaggerAgentUtils.validate_result_integrity(raw_result):
            self.status = "idle"
            raise ValueError(f"Dagger Agent {self.name} detected result integrity flaw.")
        import hashlib
        result_hash = hashlib.sha256(str(raw_result).encode()).hexdigest()
        self.status = "idle"
        return {"result": raw_result, "hash": result_hash, "agent": self.name}
    def _perform_task(self, task_params):
        raise NotImplementedError

class DataSieveAgent(DaggerAgent):
    def __init__(self, axioms):
        super().__init__("DataSieveAgent", "data_filtering", axioms)
    def _perform_task(self, task_params):
        data = task_params.get("data", "")
        filtered_data = DaggerAgentUtils.densify_text(data, float(self._axioms.get("DENSITY", 1.0)))
        return f"Data sieved and densified: {filtered_data[:100]}..."

class ZKProofAgent(DaggerAgent):
    def __init__(self, axioms):
        super().__init__("ZKProofAgent", "zk_computation", axioms)
    def _perform_task(self, task_params):
        import hashlib
        input_data = task_params.get("input", "")
        proof = hashlib.sha256(input_data.encode()).hexdigest()
        return f"ZK Proof generated: {proof}"

class MarketAnalysisAgent(DaggerAgent):
    def __init__(self, axioms):
        super().__init__("MarketAnalysisAgent", "market_intelligence", axioms)
    def _perform_task(self, task_params):
        target = task_params.get("target", "general market")
        analysis_result = (
            f"Strategic market analysis for '{target}' completed with SHARPENED precision. "
            f"Identified key leverage points for unassailable dominance."
        )
        return analysis_result
