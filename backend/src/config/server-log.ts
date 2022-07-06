import { ConfigService } from './configuration';

export async function serverStatus(app): Promise<void> {
  const configService = new ConfigService();
  await app
    .listen(configService.get('server').port)
    .then(() => {
      console.log(`API running on port ${configService.get('server').port}`);
    })
    .catch(() => {
      console.log(
        `Unable to stabilish connection on port ${
          configService.get('server').port
        }`,
      );
    });
}
