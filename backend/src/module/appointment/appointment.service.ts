import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { CreateAppointmentInput } from './dtos/inputs/create-appointment-input';
import { Appointment } from './dtos/models/appointment.model';

@Injectable()
export class AppointmentService {
  constructor(
    @InjectModel(Appointment.name)
    private readonly appointmentModel: Model<Appointment>,
  ) {}

  async createAppointment(createAppointmentInput: CreateAppointmentInput) {
    const appointment = new this.appointmentModel(createAppointmentInput);
    return appointment.save();
  }

  async getAllAppointments() {
    return await this.appointmentModel.find();
  }

  async getAppointmentById(id: string) {
    const appointment = await this.appointmentModel.findOne({ _id: id }).exec();

    if (!appointment) {
      throw new NotFoundException(`Appointment ${id} not found`);
    }
    return appointment;
  }
}
