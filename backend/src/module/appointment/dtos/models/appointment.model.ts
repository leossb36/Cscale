import { ObjectType, Field } from '@nestjs/graphql';
import { Date, Schema as MongooseSchema } from 'mongoose';
import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
@Schema()
@ObjectType()
export class Appointment {
  @Field(() => String)
  _id: MongooseSchema.Types.ObjectId;

  @Prop({ require: true, type: Date })
  @Field(() => Date, { description: 'Appointment date ' })
  appointDate: { type: Date };
}

export const AppointmentSchema = SchemaFactory.createForClass(Appointment);
