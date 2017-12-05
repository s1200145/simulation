# coding: utf-8
import numpy as np
import scipy as sp
import scipy.constants
import math
import sys
import os

class Model:
	def __init__(self, m, w, rw, rr):
		self.mass = m
		self.wheel = w
		self.rod_w = rw
		self.rod_r = rr
		self.gravity =  sp.constants.g
		self.F = 50
		self.rho = 1.0
		self.f_r = np.zeros((2,2), dtype=float)
		self.f_s = np.zeros((2,2), dtype=float)
		self.f_mg = np.zeros((2,2), dtype=float)
		self.f_f = np.zeros((2,2), dtype=float)

	def  f_rotate(self, theta):
		self.f_r[0,0] = self.F*math.cos(math.radians(theta))*self.rod_w
		self.f_r[1,0] = self.F*(-math.sin(math.radians(theta)))*self.rod_w

	def f_soil(self,  height):
		self.f_s[0,0] = 0.0
		self.f_s[1,0] = self.rho * self.gravity * self.rod_w *(height * self.wheel * self.rod_r - 1.0/2.0 * self.mass*self.rod_r)

	def f_gravity(self):
		self.f_mg[0,0]=0.0
		self.f_mg[1,0]=self.mass*self.gravity

	def f_friction(self):
		# determine this value from experiment
		self.f_f[0,0] = 1.0
		self.f_f[1,0] = 1.0

	def print_t(self, elps_t):
		print(str(elps_t), end=" ")
		print(str(self.f_r[0,0]) + " " + str(self.f_r[1,0]), end=" ")
		print(str(self.f_s[0,0]) + " " + str(self.f_s[1,0]), end=" ")
		print(str(self.f_mg[0,0]) + " " + str(self.f_mg[1,0]), end=" ")
		print(str(self.f_f[0,0]) + " " + str(self.f_f[1,0]))

	def print_angle(self, theta):
		print(str(theta), end=" ")
		print(str(self.f_r[0,0]) + " " + str(self.f_r[1,0]), end=" ")
		print(str(self.f_s[0,0]) + " " + str(self.f_s[1,0]), end=" ")
		print(str(self.f_mg[0,0]) + " " + str(self.f_mg[1,0]), end=" ")
		print(str(self.f_f[0,0]) + " " + str(self.f_f[1,0]))


if  __name__ == "__main__":
	# declaration of model for computation
	# Model m(mass, wheel_r, rod_w, rod_r)
	m = Model(0.004, 0.084, 0.06, 0.004)

	# front angle and rear angle
	theta_f = 28.0
	theta_r = -28.0
	# separation
	n = 1000
	# height from topsoil to center of rod
	h = 0.01
	# initial angle
	theta = theta_f
	# end time for computation
	end_t = 10
	t = 0.0
	
	# the amount of change
	dtheta = (theta_f - theta_r) / n
	dt = end_t / n
	dh = 0.0

	i = 0
	while True:
		m.f_rotate(theta)
		m.f_friction()
		m.f_soil(h)
		m.f_gravity()
		t = dt * i
		theta -= dtheta
		h += dh
		if(t >= end_t):
			break
		# m.print_t(t)
		m.print_angle(theta)
		i += 1
