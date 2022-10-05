import { HttpException, HttpStatus } from '@nestjs/common';

export class ExceptionHandler extends HttpException {
  constructor(message: string, status: HttpStatus) {
    super(message, status);
  }

  send() {
    console.log('Error:', this.message);
  }
}
