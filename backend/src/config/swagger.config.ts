import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';

export async function swaggerConfiguration(app: any) {
  const swaggerSetup = new DocumentBuilder()
    .setTitle('Ceremonial Scale API')
    .setDescription('Ceremonial Scale API')
    .setVersion('1.0')
    .addBearerAuth()
    .build();

  const document = SwaggerModule.createDocument(app, swaggerSetup);
  SwaggerModule.setup('api', app, document);
}
