import graphene
from graphene_django import DjangoObjectType
from courses.models import Category, Level, Course

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'courses_category', 'courses_subcategory')

class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class CreateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)
    
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, input=None):
        category_instance = Category(name=input.name)
        category_instance.save()
        return CreateCategory(category=category_instance)

class LevelType(DjangoObjectType):
    class Meta:
        model = Level
        fields = ('id', 'name', 'courses_level')

class LevelInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class CreateLevel(graphene.Mutation):
    class Arguments:
        input = LevelInput(required=True)

    level = graphene.Field(LevelType)

    @staticmethod
    def mutate(root, info, input=None):
        level_instance = Level(name=input.name)
        level_instance.save()
        return CreateLevel(level=level_instance)

class CourseType(DjangoObjectType):
    class Meta:
        model = Course

class Query(graphene.ObjectType):
    courses = graphene.List(CourseType)

    def resolve_courses(self, info):
        return Course.objects.all()

class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_level = CreateLevel.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)