function setup()
	Camera:registerSystem("FaceTracking")
	Camera:startSystemProcessing()
	sleep(2)
end

function loop()
	response = Camera:getFaceCenter()
	if(response == nil) then
		print("no face detect")
	else
		print("center x: " .. response[0] .. " center y: " .. response[1])
		print("refresh rate: " .. Camera:getRefreshRate())
		Robot:execute{action="look_at",tags={"eye"},hor=-response[0],vert=-response[1]}
		

	end
	
	
	sleep(0.5)

end

function quit()
	Camera:stopSystemProcessing()
	Camera:unregisterAllSystem()
end