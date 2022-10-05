export class ConfigurationServer {
  private readonly envConfig: { [key: string]: any } = null;

  constructor() {
    this.envConfig = {};
    this.envConfig.port = +process.env.API_NODE_PORT;
    this.envConfig.mongo = {
      url: process.env.MONGODB_URL,
    };
  }

  get(key: string): any {
    return this.envConfig[key];
  }
}
