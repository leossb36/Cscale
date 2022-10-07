import { Args, Mutation, Query, Resolver } from '@nestjs/graphql';
import { AppointmentService } from './appointment.service';
import { CreateAppointmentInput } from './dtos/inputs/create-appointment-input';
import { Appointment } from './dtos/models/appointment.model';

@Resolver(() => Appointment)
export class AppointmentResolver {
  constructor(private readonly appointmentService: AppointmentService) {}

  @Query(() => [Appointment])
  async getAllAppointments() {
    return await this.appointmentService.getAllAppointments();
  }

  @Query(() => [Appointment])
  async getAppointmentById(@Args('id', { type: () => String }) id: string) {
    return await this.appointmentService.getAppointmentById(id);
  }

  @Mutation(() => Appointment)
  async createAppointment(@Args('data') data: CreateAppointmentInput) {
    return await this.appointmentService.createAppointment(data);
  }
}
