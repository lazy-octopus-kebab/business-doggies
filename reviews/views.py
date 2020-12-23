from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DeleteView

from .models import Review, ReviewRating


class ReviewListView(ListView):
	model = Review
	#<app>/<model>_<viewtype>.html
	template_name = 'reviews/profile.html'
	context_object_name = 'reviews'
	

class ReviewCreateView(LoginRequiredMixin, CreateView):
	model = Review
	#<app>/<model>_<viewtype>.html
	fields = ['text']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Review
	success_url = 'reviews/profile.html'
	#<app>/<model>_<viewtype>.html

	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False


class ReviewRatingListView(ListView):
	model = ReviewRating
	#<app>/<model>_<viewtype>.html
	template_name = 'reviews/profile.html'
	context_object_name = 'reviews_rating'
	

class ReviewRatingCreateView(LoginRequiredMixin, CreateView):
	model = ReviewRating
	#<app>/<model>_<viewtype>.html
	fields = ['text', 'rating']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ReviewRatingDeleteView(DeleteView):
	model = ReviewRating
	success_url = 'reviews/profile.html'
	#<app>/<model>_<viewtype>.html

	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False

