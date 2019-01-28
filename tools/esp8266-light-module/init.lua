
function startup()
	if file.open("init.lua") == nil then
  	print("init.lua deleted or renamed")
  else
   	print("Running")
    file.close("init.lua")
    -- the actual application is stored in 'application.lua'
    print("-- IP addr --")
    print(wifi.sta.getip())
    dofile("application.lua")
	end
end


print("You have 3 seconds to abort")
print("Waiting...")
tmr.create():alarm(3000, tmr.ALARM_SINGLE, startup)
