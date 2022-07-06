export class ConfigService {
  private readonly envConfig: { [key: string]: any } = null;

  constructor() {
    this.envConfig = {};
    this.envConfig.mongo = {
      url: process.env.MONGO_URL,
    };
    this.envConfig.server = {
      port: process.env.API_NODE_PORT,
    };
  }

  get(key: string): any {
    return this.envConfig[key];
  }
}
