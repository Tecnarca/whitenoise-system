from opendp.whitenoise.evaluation.privacyalgorithm._base import PrivacyAlgorithm
from opendp.whitenoise.evaluation.params._privacy_params import PrivacyParams
from opendp.whitenoise.evaluation.params._eval_params import EvaluatorParams
from opendp.whitenoise.evaluation.params._benchmark_params import BenchmarkParams
from opendp.whitenoise.evaluation.metrics._metrics import Metrics
from opendp.whitenoise.evaluation.metrics._benchmark_metrics import BenchmarkMetrics
from abc import ABC, abstractmethod

class Benchmarking(ABC):
	"""
	Interface for benchmark DP implementations to interface with tests available
	in evaluator. Evaluator tests for various properties of DP implementation
	like privacy, accuracy, utility and bias. Benchmark will run the evaluator
	for multiple parameters like epsilon, dataset size etc. 
	"""
	@abstractmethod
	def benchmark(self, benchmark_params : BenchmarkParams) -> BenchmarkMetrics:
		"""
		Benchmarks properties of privacy algorithm DP implementations using metrics
			- Privacy Promise
			- Accuracy Promise
			- Utility Promise
			- Bias Promise
		
		d1 and d2 are neighboring datasets
		algorithm is the DP implementation object
		Returns a metrics object
		"""
		pass