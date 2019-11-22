doctors = ['Doctor 1', 'Doctor 2', 'Doctor 3', 'Doctor 4', 'Doctor 5']

times = [str(n) for n in range(8, 19)]

neighbors = {}
neighbors['8'] = ['9']
neighbors['9'] = ['8', '10']
neighbors['10'] = ['9', '11']
neighbors['11'] = ['10', '12']
neighbors['12'] = ['11', '13']
neighbors['13'] = ['12', '14']
neighbors['14'] = ['13', '15']
neighbors['15'] = ['14', '15']
neighbors['16'] = ['15', '17']
neighbors['17'] = ['16', '18']
neighbors['18'] = ['17', '19']
neighbors['19'] = ['18']

appointments = {}


def promising(time, doctor):
    for neighbor in neighbors.get(time):
        color_of_neighbor = appointments.get(neighbor)
        if color_of_neighbor == doctor:
            return False

    return True


def get_doctor_for_appt(time):
    for doctor in doctors:
        if promising(time, doctor):
            return doctor


if __name__ == '__main__':
    for time in times:
        appointments[time] = get_doctor_for_appt(time)

    appointments_per_doctor = {}

    for time, doctor in appointments.items():
        if doctor in appointments_per_doctor.keys():
            appointments_per_doctor[doctor].append(time)
        else:
            appointments_per_doctor[doctor] = [time]

    print(appointments_per_doctor)
