from django import forms
from .models import Survey
from django.db import models

class ProductForm(forms.ModelForm):
	class Meta:
		model = Survey
		fields = [
			'lab', 
			'q0','q1','q2','q3','f1','f2',
			'q4','q5','q6','q7','q8','f3',
			'q9','q10','q11','f4',
			'q12','q13','q14','f5'
		]
		labels = {
			"q0" : "The labs helped me understand the lecture material.",
			"q1" : "The labs taught me new skills.",
			"q2" : "The labs taught me to think creatively.",
			"q3" : "I would be able to repeat the labs without help.",
			"f1" : "What was your favorite aspect of lab?",
			"f2" : "What about the lab would you like to see improved?",
			"q4" : "The lab instructor was supportive.",
			"q5" : "The lab instructor was approachable.",
			"q6" : "The lab instructor was able to answer my questions.",
			"q7" : "The lab instructor helped me reach a clear understanding of key concepts.",
			"q8" : "The lab instructor fostered a mutually respectful learning environment.",
			"f3" : "What, if anything, could the lab instructor do to improve the experience?",
			"q9" : "The amount of lab equipment was sufficient.",
			"q10" : "The available space was sufficient for the lab activities.",
			"q11" : "If lab equipment or setups were not functioning properly, adequate support was available to rectify the situation.",
			"f4" : "What, if anything, could the lab instructor do to improve the experience?",
			"q12" : "On average, the approximate number of hours completing a lab was",
			"q13" : "How many hours did you spend preparing for the lab?",
			"q14" : "How many hours did you spend writing lab reports outside the designated lab period?",
			"f5" : "What feedback would you give the lecture section instructor (not the lab TA) about",

		}

