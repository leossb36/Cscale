import { Field, InputType } from '@nestjs/graphql';

@InputType()
export class CreateAppointmentInput {
  @Field()
  appointmentDate: Date;
}
