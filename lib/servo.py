from machine import Pin,PWM
class Servo:
	__servo_pwm_freq=50;__min_u10_duty=36;__max_u10_duty=123;min_angle=0;max_angle=180;current_angle=.001;is_enabled=True
	def __init__(A,pin,enOrDi=True):A.is_enabled=enOrDi;A.__initialise(pin)
	def update_settings(A,servo_pwm_freq,min_u10_duty,max_u10_duty,min_angle,max_angle,pin):
		if A.is_enabled:A.__servo_pwm_freq=servo_pwm_freq;A.__min_u10_duty=min_u10_duty;A.__max_u10_duty=max_u10_duty;A.min_angle=min_angle;A.max_angle=max_angle;A.__initialise(pin)
	def move(A,angle):
		B=angle
		if A.is_enabled:
			B=round(B,2)
			if B<A.min_angle:B=A.min_angle
			elif B>A.max_angle:B=A.max_angle
			if abs(B-A.current_angle)<.1:return
			A.current_angle=B;C=A.__angle_to_u10_duty(B);A.__motor.duty(C)
	def __angle_to_u10_duty(A,angle):
		if A.is_enabled:return int((angle-A.min_angle)*A.__angle_conversion_factor)+A.__min_u10_duty
	def __initialise(A,pin):
		if A.is_enabled:A.current_angle=-.001;A.__angle_conversion_factor=(A.__max_u10_duty-A.__min_u10_duty)/(A.max_angle-A.min_angle);A.__motor=PWM(Pin(pin));A.__motor.freq(A.__servo_pwm_freq)