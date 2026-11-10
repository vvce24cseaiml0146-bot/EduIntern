from nicegui import ui
from services.internship_api import get_internships
import os


# Website colours
def set_colours():
    ui.colors(
        primary='#293D70',
        secondary='#A8B5D8',
        accent='#8176B5'
    )


# Navigation bar
def navbar():
    with ui.header().classes(
        'items-center justify-between bg-[#293D70] px-8'
    ):
        ui.label('EduIntern').classes(
            'text-2xl font-bold text-white'
        )

        with ui.row().classes('items-center gap-6'):
            ui.link('Home', '/').classes('text-white')
            ui.link('Internships', '/internships').classes('text-white')
            ui.link('About', '/about').classes('text-white')


# Homepage
@ui.page('/')
def home():

    set_colours()
    navbar()

    with ui.column().classes(
        'w-full items-center justify-center py-24 bg-[#F2F4FA]'
    ):
        ui.label('Discover Opportunities.').classes(
            'text-5xl font-bold text-[#293D70] text-center'
        )

        ui.label('Build Your Future.').classes(
            'text-4xl font-bold text-[#293D70] text-center'
        )

        ui.label(
            'Explore internship opportunities from companies across India.'
        ).classes(
            'text-lg text-gray-600 mt-4 text-center'
        )

        ui.button(
            'Explore Internships',
            on_click=lambda: ui.navigate.to('/internships')
        ).classes('mt-6 px-8 py-3')

    with ui.column().classes('w-full items-center py-16'):
        ui.label('Why Choose EduIntern?').classes(
            'text-3xl font-bold text-[#293D70]'
        )

        with ui.row().classes('justify-center gap-6 mt-8 flex-wrap'):
            features = [
                ('Explore', 'Discover internships across India'),
                ('Discover', 'Find opportunities in technical domains'),
                ('Apply', 'Visit original company application pages')
            ]

            for heading, description in features:
                with ui.card().classes('w-64 p-5'):
                    ui.label(heading).classes(
                        'text-xl font-bold text-[#293D70]'
                    )
                    ui.label(description).classes('text-gray-600')


# Internships page
@ui.page('/internships')
def internships_page():

    set_colours()
    navbar()

    with ui.column().classes('w-full items-center py-10'):

        ui.label('Explore Internships').classes(
            'text-4xl font-bold text-[#293D70]'
        )

        ui.label(
            'Find internship opportunities from different companies.'
        ).classes('text-gray-600 mt-2')

        try:
            jobs = get_internships()

            locations = sorted({
                str(job.get('city_tag') or 'Not specified')
                for job in jobs
            })

            # Search and filter
            with ui.row().classes(
                'w-full justify-center items-center gap-4 mt-8 flex-wrap'
            ):
                search = ui.input(
                    label='Search internships',
                    placeholder='Enter company or job title'
                ).classes('w-80')

                location_filter = ui.select(
                    options=['All Locations'] + locations,
                    value='All Locations',
                    label='Filter by location'
                ).classes('w-64')

            # Internship results
            with ui.column().classes('w-full items-center mt-6') as results:

                pass

            def display_jobs():

                results.clear()

                search_text = (search.value or '').lower()
                selected_location = location_filter.value

                filtered_jobs = [
                    job for job in jobs
                    if (
                        search_text in str(job.get('title', '')).lower()
                        or search_text in str(job.get('company', '')).lower()
                        or search_text in str(job.get('city_tag', '')).lower()
                    )
                    and (
                        selected_location == 'All Locations'
                        or str(job.get('city_tag') or 'Not specified')
                        == selected_location
                    )
                ]

                with results:

                    ui.label(
                        f'Showing {len(filtered_jobs)} of {len(jobs)} internships'
                    ).classes('text-lg font-bold mb-4')

                    if not filtered_jobs:
                        ui.label(
                            'No internships found. Try another search.'
                        ).classes('text-gray-600')

                    with ui.row().classes(
                        'w-full justify-center flex-wrap gap-6 p-4'
                    ):

                        for job in filtered_jobs:

                            with ui.card().classes('w-80 p-5'):

                                ui.label(
                                    job.get('title', 'Internship')
                                ).classes(
                                    'text-xl font-bold text-[#293D70]'
                                )

                                ui.label(
                                    job.get(
                                        'company',
                                        'Company not available'
                                    )
                                ).classes(
                                    'text-lg font-semibold'
                                )

                                ui.label(
                                    'Location: ' +
                                    str(job.get('city_tag', 'Not specified'))
                                ).classes('text-gray-600')

                                apply_url = job.get('url')

                                if apply_url:
                                    ui.link(
                                        'Apply Now',
                                        apply_url
                                    ).classes(
                                        'text-blue-700 font-bold mt-3'
                                    )

            # Update results when filters change
            search.on_value_change(lambda: display_jobs())
            location_filter.on_value_change(lambda: display_jobs())

            display_jobs()

        except Exception as error:

            ui.label(
                'Unable to load internships. Please try again.'
            ).classes('text-red-600')

            print('Error:', error)


# About page
@ui.page('/about')
def about_page():

    set_colours()
    navbar()

    with ui.column().classes(
        'w-full items-center py-20 px-8'
    ):
        ui.label('About EduIntern').classes(
            'text-4xl font-bold text-[#293D70]'
        )

        ui.label(
            'EduIntern helps students discover internship '
            'opportunities from companies across India.'
        ).classes(
            'text-lg text-gray-600 text-center mt-4'
        )


# Run application
ui.run(
    title='EduIntern',
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 8080)),
    reload=False
)