import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { swaggerConfiguration } from '@config/swagger.config';
import { serverStatus } from '@config/server-log';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  swaggerConfiguration(app);
  serverStatus(app);
}
bootstrap();
