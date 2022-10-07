import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { CreateUserInput } from './dtos/inputs/create-user-input';
import { User } from './dtos/models/user.model';

@Injectable()
export class UserService {
  constructor(
    @InjectModel(User.name)
    private readonly userModel: Model<User>,
  ) {}

  async createUser(createUserInput: CreateUserInput) {
    const user = new this.userModel(createUserInput);
    return user.save();
  }

  async getAllUsers() {
    return await this.userModel.find();
  }

  async getUserById(id: string) {
    const user = await this.userModel.findOne({ _id: id }).exec();

    if (!user) {
      throw new NotFoundException(`User ${id} not found`);
    }
    return user;
  }
}
