import { Args, Mutation, Query, Resolver } from '@nestjs/graphql';
import { UserService } from './user.service';
import { CreateUserInput } from './dtos/inputs/create-user-input';
import { User } from './dtos/models/user.model';

@Resolver(() => User)
export class UserResolver {
  constructor(private readonly userService: UserService) {}

  @Query(() => [User])
  async getAllUsers() {
    return await this.userService.getAllUsers();
  }

  @Query(() => [User])
  async getUserById(@Args('id', { type: () => String }) id: string) {
    return await this.userService.getUserById(id);
  }

  @Mutation(() => User)
  async createUser(@Args('data') data: CreateUserInput) {
    return await this.userService.createUser(data);
  }
}
