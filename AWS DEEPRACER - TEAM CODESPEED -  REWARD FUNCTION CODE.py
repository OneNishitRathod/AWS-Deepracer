def reward_function(params):

    # Read input parameters

    distance_from_center = params['distance_from_center']

    track_width = params['track_width']

  
    all_wheels_on_track = params['all_wheels_on_track']

    speed = params['speed']

    SPEED_THRESHOLD = 1


    # Calculate 5 marks father away from the center line

    marker_1 = 0.1 * track_width

    marker_2 = 0.20 * track_width

    marker_3 = 0.30 * track_width

    marker_4 = 0.40 * track_width

    marker_5 = 0.5 * track_width
 

    # Give higher reward if the car is closer to center line 

    if distance_from_center <= marker_1 and all_wheels_on_track:

        reward = 3.0

    elif distance_from_center <= marker_2 and all_wheels_on_track:

        reward = 2.5

    elif distance_from_center <= marker_3 and all_wheels_on_track:

        reward = 1.5

    elif distance_from_center <= marker_4 and all_wheels_on_track:

        reward = 1

    elif distance_from_center <= marker_5 and all_wheels_on_track:

        reward = 0.5

    else:

        reward = 1e-3  # likely crashed/ close to off track


    if speed < SPEED_THRESHOLD:

        # Penalize if the car goes too slow

        reward = reward + 0.5

    else:

        # High reward if the car stays on track and goes fast

        reward = reward + 1.0
        

    return float(reward)