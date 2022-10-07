import { Module } from '@nestjs/common';
import { AppointmentModule } from './module/appointment/appointment.module';
import { CommonModule } from './module/common/common.module';
import { UsersModule } from './module/user/user.module';

const gqlImports = [CommonModule, UsersModule, AppointmentModule];

@Module({
  imports: [...gqlImports],
})
export class AppModule {}
