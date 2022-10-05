import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { ConfigurationServer } from './config/configuration';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const port: number = new ConfigurationServer().get('port');

  app.listen(port).then(() => {
    console.log(`🚀 HTTP server running on ${port} 🚀`);
  });
}
bootstrap();
