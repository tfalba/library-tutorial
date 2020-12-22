from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Project, ProjectImage

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
#admin.site.register(Project)
#admin.site.register(ProjectImage)

class ProjectImageInline(admin.TabularInline):
  model = ProjectImage
  extra = 0

#@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('title', 'brief_description', 'languages')
  inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)

#@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
  list_display = ('link_to_image', 'status')

admin.site.register(ProjectImage, ProjectImageAdmin)  


class BookInline(admin.TabularInline):
  model = Book
  extra = 0


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
  fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
  inlines = [BookInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
  model = BookInstance
  extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')
  inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  list_filter = ('status', 'due_back')

  fieldsets = (
      (None, {
        'fields': ('book', 'imprint', 'id')
      }),
      ('Availability', {
        'fields': ('status', 'due_back')
      }),
  )
  #note - could not have 'id' showing for instance if didn't want to overwrite it


