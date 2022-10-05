import { Field, ObjectType } from '@nestjs/graphql';

@ObjectType()
export class Appointment {
  @Field()
  appointmentDate: Date;
}
