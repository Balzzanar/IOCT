--                     --
--      Constants      --
--                     --

-- true == on, false == off
GPIO_LED_PIN = 7
GPIO_MAIN_CONTROL_STATUS = false;

GPIO_LED_ON = gpio.LOW;
GPIO_LED_OFF = gpio.HIGH;


UNIQUE_CLIENT_ID = "ESP001"
MQTT_TOPIC_STATUS = UNIQUE_CLIENT_ID .. "-status"
MQTT_TOPIC_CMD = UNIQUE_CLIENT_ID .. "-cmd"
MQTT_CMD_OPTION_ON = "1"
MQTT_CMD_OPTION_OFF = "0"

--                     --
--      Globals        --
--                     --
local lastToggleTime = 0
local isConnected = false

--                     --
--      Functions      --
--                     --
function setRelay(status)
-- true == on, false == off
	if (status)then
		gpio.write(GPIO_LED_PIN, GPIO_LED_ON)
		print("ON");
	else
		gpio.write(GPIO_LED_PIN, GPIO_LED_OFF)
		print("OFF");
	end
end

function toggle()
	if (GPIO_MAIN_CONTROL_STATUS)then
		GPIO_MAIN_CONTROL_STATUS = false;
		setRelay(false)
	else
		GPIO_MAIN_CONTROL_STATUS = true;
		setRelay(true)
	end
end

--                       --
--      Main Script      --
--                       --

-- Setup the GPIO pins
print("Start the main loop for toggling")

-- Pin definition
local duration = 3000

-- Initialising pin
gpio.mode(GPIO_LED_PIN, gpio.OUTPUT)


-- Create an interval
tmr.alarm(0, duration, 1, function ()
	toggle(); 
end)



