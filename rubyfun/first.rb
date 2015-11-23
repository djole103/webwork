class Greeter
	def initialize(name="World")
		@name = name
	end
	def say_hello
		puts "hello #{@name}!"
	end
	def say_bye
		puts "Bye #{@name}, come back sooon"
	end
end

g = Greeter.new("Scott")
g.say_hello
g.say_bye
