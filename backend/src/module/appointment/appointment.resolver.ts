import { Args, Mutation, Query, Resolver } from '@nestjs/graphql';
import { CreateAppointmentInput } from './dtos/inputs/create-appointment-input';
import { Appointment } from './dtos/models/appointment.model';

@Resolver(() => Appointment)
export class AppointmentResolver {
  @Query(() => [Appointment])
  async appointments() {
    return [
      {
        appointmentDate: new Date(),
      },
    ];
  }

  @Mutation(() => Appointment)
  async createAppointment(@Args('data') data: CreateAppointmentInput) {
    const appointment = {
      appointmentDate: data.appointmentDate,
    };

    return appointment;
  }
}
