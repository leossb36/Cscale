import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { AppointmentResolver } from './appointment.resolver';
import { AppointmentService } from './appointment.service';
import {
  Appointment,
  AppointmentSchema,
} from './dtos/models/appointment.model';

@Module({
  imports: [
    MongooseModule.forFeature([
      {
        name: Appointment.name,
        schema: AppointmentSchema,
      },
    ]),
  ],
  providers: [AppointmentResolver, AppointmentService],
})
export class AppointmentModule {}
