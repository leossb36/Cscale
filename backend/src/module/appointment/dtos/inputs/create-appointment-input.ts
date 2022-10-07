import { InputType, Field } from '@nestjs/graphql';

@InputType()
export class CreateAppointmentInput {
  @Field(() => Date, { description: 'appointment date' })
  appointDate: Date;
}
