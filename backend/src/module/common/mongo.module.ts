import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { ConfigurationServer } from 'src/config/configuration';

@Module({
  imports: [
    MongooseModule.forRootAsync({
      useFactory: async () => ({
        uri: new ConfigurationServer().get('mongo').url,
      }),
    }),
  ],
})
export class MongoModule {}
