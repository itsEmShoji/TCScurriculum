# Insert Code

# Insert Code

# Insert Code
  # Insert Code

# Insert Code

appt_graph['7'] = ['8', '11']
appt_graph['8'] = ['9', '7', '12']
appt_graph['9'] = ['10', '8', '13']
appt_graph['10'] = ['11', '9', '14']
appt_graph['11'] = ['12', '10','7']
appt_graph['12'] = ['13', '11','8']
appt_graph['13'] = ['14', '12','9']
appt_graph['14'] = ['15', '13','10']
appt_graph['15'] = ['16', '14']
appt_graph['16'] = ['17', '15']
appt_graph['17'] = ['18', '16']
appt_graph['18'] = ['19', '17']
appt_graph['19'] = ['18']


# Insert Code

def promising(time, doctor):
    # Insert Code
       doctor_for_neighbor_appt = appointments.get(neighbor)
        if doctor_for_neighbor_appt == doctor:
            # Insert Code
   # Insert Code


def get_doctor_for_appt(time):
    # Insert Code
        if promising(time, doctor):
            # Insert Code


if __name__ == '__main__':
    # Insert Code
         appointments[time] = get_doctor_for_appt(time)

    # Insert Code

    for time, doctor in appointments.items():
        if doctor in appointments_per_doctor.keys():
            appointments_per_doctor[doctor].append(time)
        else:
            appointments_per_doctor[doctor] = [time]

    # Insert Code